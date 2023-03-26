str_ = input()
stack_ = list()
br = True
for s in str_:
    if not stack_ and (s == ')' or (s == ']') or (s == '}')):
        br *= False
        break
    if not stack_:
        stack_.append(s)
    else:
        if s == '(' or s == '[' or s == '{':
            stack_.append(s)
        elif s == ')':
            if stack_[-1] == '(':
                stack_.pop()
            else:
                br *= False
        elif s == ']':
            if stack_[-1] == '[':
                stack_.pop()
            else:
                br *= False
        elif s == '}':
            if stack_[-1] == '{':
                stack_.pop()
            else:
                br *= False

if not stack_ and br:
    print('yes', end='')
else:
    print('no', end='')


