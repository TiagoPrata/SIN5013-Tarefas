from functools import reduce
import operator


def test(A, vf, set1):
    values = [a*b for a,b in zip(A,set1)]
    sum = reduce(operator.add, values)
    
    return (sum == vf)


def get_diff_results(results):
    final = ''
    A = results[0]
    B = results[1]
    for i in range(0, len(A)):
        if A[i] != B[i]:
            final += '?'
        elif A[i] == -1:
            final += '-'
        else:
            final += '+'

    return final


def list_exponential(n,set1,A,vf,results=[]):
    if n == 0:
        print(set1)
        if test(A, vf, set1):
            results.append(set1)
    else:
        n-=1
        list_exponential(n, [1]+set1, A, vf)
        list_exponential(n, [-1]+set1, A, vf)
        
    # TODO Corrigir
    if (len(results) > 1) and (n == 0):
        print(get_diff_results(results))


if __name__=='__main__':
    A = [1,2,3,4,5]
    vf = 7
    list_exponential(5,[],A,vf)