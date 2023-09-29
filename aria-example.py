import '.src/qshaptools/cqshap.py'

# a callable that takes as argument a coalition S, that is a list of numbers (from 0 to N-1) and returns a float, the value of the respective coalition
def value_fun(S):
  if(len(S)) < 2: 
    return 0 # in this dummy example, all coallitions with less than two players generate no value
  else:
    return 10.0 # in this dummy example, all coallitions with more than one player generates 10.0 value

N = 5 #the number of players
shap_sample_frac = 1 #the % of coalitions that are calculated (optional argument for ClassicalShapleyValues)
shap_sample_reps = 1 #the number of times that the value function is evaluated to take into account noise. Choose a higher value for a noisy value function. By default, its set to 1. (optional argument for ClassicalShapleyValues)

sv = ClassicalShapleyValues(N, value_fun)()
display(sv)
