"""
BUbbles and buckets
Andrea, Carlos and Marcelo are close friends and spend their weekends by the swimming pool. While Andrea gets a suntan, both friends play Bubbles. Andrea, a very smart computer scientist, has already told them that she does not understand why they spend so much time playing a game so simple.

Using her laptop, Carlos and Marcelo generate a random integer N and a sequence, also random, which is a permutation from 1, 2, ..., N.

The game then begins. The players play by turns, and at each turn a player makes a move. Marcelo is always the first to play.A move consists of choosing one pair of consecutive elements that are out of order in the sequence, and swapping both elements. For example, given the sequence 1, 5, 3, 4, 2, a player may swap 3 and 5 or 4 and 2, but cannot swap 3 and 4 nor 5 and 2. Continuing with the example, if the player decides to swap 5 and 3, the new sequence will be 1, 3, 5, 4, 2.

Sooner or later, the sequence will be sorted. The player that cannot make a move loses. Andrea, with disdain, always says that it would be simpler to play Odd or Even, to the same effect. Your mission, in case you decide to accept it, is to determine who wins the game, given the initial permutation P.

Input
The input contains several test cases. Each test case is composed of a single line, in which all integers are separated by one space. Each line contains an integer N (2 ≤ N ≤ 105), followed by the initial sequence P = (X1, X2, ...,XN) of N distinct integers, with 1 ≤ Xi ≤ N for 1 ≤ i ≤ N.

The end of input is indicated by a line containing only one zero.

Output
For each test case in the input, your program must print a single line, containing the name of the winner, equal to Carlos or Marcelo
"""
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
  
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1
  
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
  
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
  
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
          
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
  
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
  
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
  
    return inv_count

def count_inversions(arr, n):
    temp_arr = [0]*n
    return merge_sort_and_count(arr, temp_arr, 0, n-1)

def main():
    while True:
        line = list(map(int, input().split()))
        n = line[0]
        if n == 0:
            break
        arr = line[1:]
        inversions = count_inversions(arr, n)
        if inversions % 2 == 0:
            print("Carlos")
        else:
            print("Marcelo")