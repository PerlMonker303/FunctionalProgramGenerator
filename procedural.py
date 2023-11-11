import re
import subprocess

dbg = False
MAX_DEPTH = 100
OPERATORS_SET = set({'<', '>', '<=', '>='})

term_regex = r'''(?mx)
    \s*(?:
        (?P<brackl>\()|
        (?P<brackr>\))|
        (?P<num>\-?\d+\.\d+|\-?\d+)|
        (?P<sq>"[^"]*")|
        (?P<s>[^(^)\s]+)
       )'''

def parse_sexp(sexp):
    stack = []
    out = []
    if dbg: print("%-6s %-14s %-44s %-s" % tuple("term value out stack".split()))
    for termtypes in re.finditer(term_regex, sexp):
        term, value = [(t,v) for t,v in termtypes.groupdict().items() if v][0]
        if dbg: print("%-7s %-14s %-44r %-r" % (term, value, out, stack))
        if   term == 'brackl':
            stack.append(out)
            out = []
        elif term == 'brackr':
            assert stack, "Invalid: Trouble with nesting of brackets"
            tmpout, out = out, stack.pop(-1)
            out.append(tmpout)
        elif term == 'num':
            v = float(value)
            if v.is_integer(): v = int(v)
            out.append(v)
        elif term == 'sq':
            out.append(value[1:-1])
        elif term == 's':
            out.append(value)
        else:
            raise NotImplementedError("Invalid: %r" % (term, value))
    assert not stack, "Invalid: Trouble with nesting of brackets"
    return out[0]

def print_sexp(exp):
    out = ''
    if type(exp) == type([]):
        out += '(' + ' '.join(print_sexp(x) for x in exp) + ')'
    elif type(exp) == type('') and re.search(r'[\s()]', exp):
        out += '"%s"' % repr(exp)[1:-1].replace('"', '\"')
    else:
        out += '%s' % exp
    return out


def convert_flat_list_helper(flat_list):
    if len(flat_list) == 0:
        return []

    first_element = flat_list[0]
    if first_element == '(':
        return [ convert_flat_list_helper(flat_list[1:len(flat_list)-1]) ]

    return [first_element] + convert_flat_list_helper(flat_list[1:])

def convert_flat_list_expression_to_imbricated_expression(flat_list):
    # Assumption: brackets are placed correctly
    return convert_flat_list_helper(flat_list)[0]


def compare(operator, left, right):
    if operator == '<':
        return left < right
    elif operator == '<=':
        return left <= right
    elif operator == '>':
        return left > right
    elif operator == '>=':
        return left >= right

def evaluate_expression(exp, env=None, depth=0, tokens=None):
    '''
    Recursive function for evaluating functions.
    :param exp: LISP expression to be evaluated
    :param env: dictionary holding variables and their assigned values
    :param depth: depth level in the call stack
    :param tokens: set of unique tokens identified so far
    :return: result after expression evaluation
    '''
    if depth > MAX_DEPTH:
        return f'Invalid: maximum recursion depth exceeded ({MAX_DEPTH}).'
    depth += 1

    if env == None:
        env = {}

    # Check if expression is list
    if isinstance(exp, list):
        operator = exp[0]
        tokens and tokens[0].add(operator)
        if isinstance(operator, int):
            return operator
        if operator == '+':
            return sum(evaluate_expression(e, env, depth, tokens) for e in exp[1:])
        elif operator == '-':
            if len(exp) == 2:
                return -evaluate_expression(exp[1], env, depth, tokens)
            else:
                return evaluate_expression(exp[1], env, depth, tokens) - sum(evaluate_expression(e, env, depth, tokens) for e in exp[2:])
        elif operator == '*':
            return eval('*'.join(map(str, [evaluate_expression(e,env, depth, tokens) for e in exp[1:]])))
        elif operator == '/':
            if len(exp) == 2:  # Support (/ number), which is translated to "1/number"
                return 1 / evaluate_expression(exp[1], env, depth, tokens)
            else:
                if exp[2] == 0:
                    return "Invalid: zero denominator in division."
                return evaluate_expression(exp[1], env, depth, tokens) / eval('*'.join(map(str, [evaluate_expression(e, env, depth, tokens) for e in exp[2:]])))
        elif operator == 'cond':
            for clause in exp[1:]:
                condition = clause[0]
                if condition == 't' or evaluate_expression(condition, env, depth, tokens):
                    return evaluate_expression(clause[1], env, depth, tokens)
            return None  # No conditions met, return None or handle it as needed
        elif operator in OPERATORS_SET:
            left = evaluate_expression(exp[1], env, depth, tokens)
            right = evaluate_expression(exp[2], env, depth, tokens)
            return compare(operator, left, right)
        elif operator == 'zerop':
            return evaluate_expression(exp[1], env, depth, tokens) == 0
        elif operator == 'null':
            # Check for null
            if isinstance(exp[1], list):
                return len(exp[1]) == 0
            else:
                return f"Invalid: null operator used on non-list element."
        elif operator == 'defun':
            # Define a function in the environment
            function_name = exp[1]
            function_params = exp[2]
            function_body = exp[3:][0]
            env[function_name] = (function_params, function_body)
        elif operator in env:
            function_params, function_body = env[operator]
            function_params_values = [evaluate_expression(eval_val, env, depth, tokens) for eval_val in exp[1:]]
            if len(function_params) != len(function_params_values):
                return f"Invalid: number of parameters required ({len(function_params)}) and number of parameters " \
                       f"passed ({len(function_params_values)}) for functon '{operator}' do not match."

            # Create a local environment for the function call
            local_env = dict(env)
            for i in range(len(function_params)):
                local_env[function_params[i]] = function_params_values[i]
            return evaluate_expression(function_body, local_env, depth, tokens)
        else:
            return f"Invalid: unsupported operator {operator}."
    elif exp in env:
        tokens and tokens[0].add(exp)
        return env[exp]
    else:
        # Return token
        tokens and tokens[0].add(exp)
        return exp


def eval_sexpression(sexpr, add_function_call=False, f_name="factorial", input=0):
    if add_function_call:
        params_list = ["C:\Program Files\Steel Bank Common Lisp\sbcl.exe",
                       "--noinform",  # skip printing initial strings
                       "--eval",
                       "(declaim (sb-ext:muffle-conditions cl:warning))",  # suppress warnings
                       "--eval",
                       f"{sexpr}",
                       "--eval",
                       f"(print ({f_name} {input}))",
                       "--quit",  # exit REPL after evaluation
                       "--disable-debugger"],  # if error, skip debugger
    else:
        params_list = ["C:\Program Files\Steel Bank Common Lisp\sbcl.exe",
                       "--noinform",  # skip printing initial strings
                       "--eval",
                       "(declaim (sb-ext:muffle-conditions cl:warning))",  # suppress warnings
                       "--eval",
                       f"(print {sexpr})",
                       "--quit",  # exit REPL after evaluation
                       "--disable-debugger"],  # if error, skip debugger

    try:
        result = subprocess.run(params_list[0], capture_output=True, text=True, timeout=1)  # Added timeout for infinite recursion
    except subprocess.TimeoutExpired:
        return "Invalid: timeout exception."
    if result.stderr:
        return "Invalid: " + result.stderr
    if result.stdout:
        res = result.stdout.replace("\n", "")
        return res

    return "Invalid execution."


def test(s_exp, expected_exp_parsed, expected_eval_result=0, env=None, should_be_invalid=False, verbose=False):
    tokens = [set()]
    parsed_exp = parse_sexp(s_exp)
    verbose and print(f'Parsed expression: {parsed_exp}')
    assert parsed_exp == expected_exp_parsed
    eval_result = evaluate_expression(parsed_exp, env, tokens=tokens)
    verbose and print(f'Evaluation result: {eval_result}')
    if should_be_invalid:
        assert eval_result.startswith("Invalid")
    else:
        assert eval_result == expected_eval_result
    s_exp_again = print_sexp(parsed_exp)
    verbose and print(f'Parsed expression again: {s_exp_again}')
    assert s_exp == s_exp_again


def test_function(s_exp, expected_exp_parsed, func_call_exp, expected_eval_result=0, should_be_invalid=False, verbose=False):
    # Initialise environment
    env = {}

    test(
        s_exp=s_exp,
        expected_exp_parsed=expected_exp_parsed,
        expected_eval_result=None,
        env=env,
        should_be_invalid=should_be_invalid,
        verbose=verbose
    )

    func_call_exp_parsed = parse_sexp(func_call_exp)
    verbose and print(f'Parsed function call: {func_call_exp_parsed}')
    tokens = [set()]
    eval_result = evaluate_expression(func_call_exp_parsed, env, depth=0, tokens=tokens)
    print(tokens)
    verbose and print(f'Evaluation result: {eval_result}')
    assert expected_eval_result == eval_result


def run_tests():

    # Test flat-list converter
    assert convert_flat_list_expression_to_imbricated_expression(['(', ')']) == []
    assert convert_flat_list_expression_to_imbricated_expression(['(', '1', ')']) == ['1']
    assert convert_flat_list_expression_to_imbricated_expression(['(', '1', '(', '2', ')', ')']) == ['1', ['2']]
    assert convert_flat_list_expression_to_imbricated_expression(['(', '(', '(', '(', ')', ')', ')', ')']) == [[[[]]]]

    # Test arithmetic operations
    test(
        s_exp="(+ 1 (* 5 (- 9 1)) 3 4)",
        expected_exp_parsed=['+', 1, ['*', 5, ['-', 9, 1]], 3, 4],
        expected_eval_result=48
    )

    test(
        s_exp="(* 0 100)",
        expected_exp_parsed=['*', 0, 100],
        expected_eval_result=0
    )

    test(
        s_exp="(/ 100 20)",
        expected_exp_parsed=['/', 100, 20],
        expected_eval_result=5
    )

    test(
        s_exp="(/ 100 0)",
        expected_exp_parsed=['/', 100, 0],
        should_be_invalid=True
    )

    # Test cond and comparison operators
    test(
        s_exp='(cond ((< 2 3) 5) ((>= 10 8) 15) (t "No conditions met"))',
        expected_exp_parsed=['cond', [['<', 2, 3], 5], [['>=', 10, 8], 15], ['t', 'No conditions met']],
        expected_eval_result=5,
    )

    test(
        s_exp='(cond ((< 4 3) 5) ((>= 10 8) 15) (t "No conditions met"))',
        expected_exp_parsed=['cond', [['<', 4, 3], 5], [['>=', 10, 8], 15], ['t', 'No conditions met']],
        expected_eval_result=15,
    )

    test(
        s_exp='(cond ((< 4 3) 5) ((>= 10 11) 15) (t "No conditions met"))',
        expected_exp_parsed=['cond', [['<', 4, 3], 5], [['>=', 10, 11], 15], ['t', 'No conditions met']],
        expected_eval_result="No conditions met"
    )

    # Test null
    test(
        s_exp='(cond ((null (1 2 3)) 1) (t 2))',
        expected_exp_parsed=['cond', [['null', [1, 2, 3]], 1], ['t', 2]],
        expected_eval_result=2
    )

    test(
        s_exp='(cond ((null ()) 1) (t 2))',
        expected_exp_parsed=['cond', [['null', []], 1], ['t', 2]],
        expected_eval_result=1
    )

    # Test defun on regular functions
    test(
        s_exp='(defun square (x) (* x x))',
        expected_exp_parsed=['defun', 'square', ['x'], ['*', 'x', 'x']],
        expected_eval_result=None
    )

    test_function(
        s_exp='(defun square (x) (* x x))',
        expected_exp_parsed=['defun', 'square', ['x'], ['*', 'x', 'x']],
        func_call_exp='(square 9)',
        expected_eval_result=81
    )

    # Test defun on recursive functions
    '''
    (defun factorial (n) 
        (cond ((zerop n) 1) 
        (t (* n (factorial (- n 1)))))
    )
    '''
    test_function(
        s_exp='(defun factorial (n) (cond ((zerop n) 1) (t (* n (factorial (- n 1))))))',
        expected_exp_parsed=['defun', 'factorial', ['n'], ['cond', [['zerop', 'n'], 1], ['t', ['*', 'n', ['factorial', ['-', 'n', 1]]]]]],
        func_call_exp='(factorial 5)',
        expected_eval_result=120
    )


if __name__ == '__main__':
    run_tests()
