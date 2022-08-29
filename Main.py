class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here

  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size = size
    self.lst = [None]*size

  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    # Write your code here
    if self.top == -1:
       return 1
    else :
       return 0
          
  def is_full(self):
    # Write code here
    if self.top == (self.size - 1):
      return 1
    else :
      return 0

  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    # Write your code here
    if not self.isEmpty():
      t=self.lst[self.top]
      del self.lst[self.top]
      self.top-=1
      return t

  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    # Write your code here
    if not self.is_full():
            self.top+=1
            self.lst[self.top]=operand

  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    # Write your code here
    c1=0
    c2=0
    for i in expression:
      if i.isdigit():
        c1+=1
      else:
        c2+=1
    if c1>c2 and expression[0].isdigit() and expression[1].isdigit():
      return 1
    else:
      return 0

  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    # Write your code here
    for i in expression:
      if i.isdigit():
        self.push(i)
      else:
        v1 = self.pop()
        v2 = self.pop()
        if i=='/':
          self.push(str(eval(v2 + i*2 + v1)))
        else:
          self.push(str(eval(v2 + i + v1)))
    return self.pop()

# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
