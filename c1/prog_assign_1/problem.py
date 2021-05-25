#%% Coursera c1 w1 assignment: Integer multiplication algorithms


def k_mult_rec(n1_s: str, n2_s: str, debug=False):
  """Multiply two numbers via Karatsuba's algorithm, recursively.

  Assumes n1 and n2 have same number of digits
  TODO: generalize to case where n1 and n2 have different numbers of digits

  Args:
    n1_s: first number, as string
    n2_s: second number, as string
    debug: whether to print debug information

  Returns:
    product of n1 and n2, as string
  """
  if debug:
    print(f"\nn1 = {n1_s}, n2 = {n2_s}")

  n1_len, n2_len = len(n1_s), len(n2_s)
  # base case
  if n_len == 1:
    if debug:
      print(f"BASE CASE. n1_len and n2_len SHOULD BOTH EQUAL 1")
      print(f"n1_len = {len(n1_s)}, n2_len = {len(n2_s)}")
    return str(int(n1_s) * int(n2_s))

  if debug:
    print(f"n1_len = {len(n1_s)}, n2_len = {len(n2_s)}")

  half_n1_len, half_n2_len = n1_len // 2, n2_len // 2
  a_s, b_s = n1_s[:half_n1_len], n1_s[half_n1_len:]
  c_s, d_s = n2_s[:half_n2_len], n2_s[half_n2_len:]

  if debug:
    print(f"half_num_len = {half_n_len}")
    print(f"a_len = {len(str(a_s))}, b_len = {len(str(b_s))}")
    print(f"c_len = {len(str(c_s))}, d_len = {len(str(d_s))}")
    print(f"a = {a_s}, b = {b_s}")
    print(f"c = {c_s}, d = {d_s}")

  # step 1
  ac_s = k_mult_rec(a_s, c_s, debug=debug)
  # if debug:
  #   print(f"a*c CORRECT RESULT = {int(a_s) * int(c_s)}")
  #   print(f"a*c RETURNED RESULT = {int(ac_s)}")

  # step 2
  bd_s = k_mult_rec(b_s, d_s, debug=debug)
  # if debug:
  #   print(f"b*d CORRECT RESULT = {int(b_s) * int(d_s)}")
  #   print(f"b*d RETURNED RESULT = {int(bd_s)}")

  # step 3
  a_plus_b_s = str(int(a_s) + int(b_s))
  c_plus_d_s = str(int(c_s) + int(d_s))
  # TODO: this doesn't work when arguments are of different length. Fix.
  a_plus_b_times_c_plus_d_s = k_mult_rec(a_plus_b_s, c_plus_d_s, debug=debug)
  if debug:
    print(f"a = {a_s}, b = {b_s}, c = {c_s}, d = {d_s}")
    print(f"(a+b)*(c+d) CORRECT RESULT = {int(a_plus_b_s) * int(c_plus_d_s)}")
    print(f"(a+b)*(c+d) RETURNED RESULT = {int(a_plus_b_times_c_plus_d_s)}")

  # step 4
  ad_plus_bc_s = int(a_plus_b_times_c_plus_d_s) - int(ac_s) - int(bd_s)

  # step 5
  res = str(
    ((10 ** n_len) * int(ac_s)) + ((10 ** half_n_len) * int(ad_plus_bc_s)) + int(bd_s)
  )

  return res


#%% copied solution from webb
def karat(x, y):
  if len(str(x)) == 1 or len(str(y)) == 1:
    return x * y
  else:
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    a = x // 10 ** (m2)
    b = x % 10 ** (m2)
    c = y // 10 ** (m2)
    d = y % 10 ** (m2)

    z0 = karat(b, d)
    z1 = karat((a + b), (c + d))
    z2 = karat(a, c)

    return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + (z0)


#%%
def run_test():
  # num1, num2 = "12", "34"
  # num1, num2 = "123", "456"
  num1, num2 = 1234, 5678

  # result = k_mult_rec(num1, num2, debug=True)
  result = karat(num1, num2)
  print(result)


run_test()

#%% input
# it's pi
num1 = (
  3_141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375_105_820_974_944_592
)
# it's e
num2 = (
  2_718_281_828_459_045_235_360_287_471_352_662_497_757_247_093_699_959_574_966_967_627
)

result = karat(num1, num2)
print(result)

# answer:
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
