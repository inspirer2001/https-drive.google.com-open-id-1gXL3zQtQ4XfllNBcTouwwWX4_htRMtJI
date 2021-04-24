
from typing import List, Tuple
from binascii import hexlify, unhexlify
from random import sample, shuffle
#to get the single string of one round of ciphertext
def merge_round_ciphertext(arr:List[List[str]])->List[str]:
  ans=[]
  l=""
  for i in range(len(arr[0])):
    for j in range(len(arr)):
      l=l+arr[j][i]
    ans.append(l)
    l=""
  return ans
# for clculating the change in different bits of two string for avalanche effect
def calculate_diff(arr1: List[List[str]], arr2: List[List[str]]) -> List[int]:
   different = []
   print(len(arr1[0]))
   for i in range(len(arr1[0])):
     cnt = 0
     for j in range(len(arr1)):
       for (a,b) in zip(arr1[j][i], arr2[j][i]):
         if(a != b):
           cnt += 1
     different.append(cnt)
   return different
def permutation(s:str,arr:List[int],n: int) ->str:
  ans = ""
  for i in range(n):
    ans+=s[arr[i]-1]
  return ans
# for getting xor of two strings.
def XOR(x: str, y: str) -> str:
    ans = ""
    for i in range(len(x)):
        if (x[i] == y[i]):
          ans += '0'
        else:
          ans += '1'
    return ans

def BinaryToDecimal(binary:str)->int:    
     strin = int(binary, 2)
     return(strin)
def bin_text(bin_data:str)->str:
  str_data =''
  for i in range(0, len(bin_data), 8):
      
    # slicing the bin_data from index range [0, 7]
    # and storing it as integer in temp_data
     temp_data = (bin_data[i:i + 8])
       
    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
     decimal_data = BinaryToDecimal(temp_data)
       
    # Deccoding the decimal value returned by 
    # BinarytoDecimal() function, using chr() 
    # function which return the string corresponding 
    # character for given ASCII value, and store it 
    # in str_data
     str_data = str_data + chr(decimal_data) 
  return str_data

def shift_towards_left(x: str, shift_by: int) -> str:
    ans =  x[shift_by:] + x[:shift_by]
    return ans 

def text_hex(txt: str) -> str:
    return hexlify(txt.encode()).decode()

#hexadecimal to text format
def hex_text(txt: str) -> str:
    return unhexlify(txt.encode()).decode()



def hex_bin(txt: str) -> str:
      return bin(int(txt,16))[2:]



def bin_hex(txt: str) -> str:
      return hex(int(txt,2))[2:]
def PC_1_generator(size: int) -> List[int]:
   ans = [x for x in range(1,size+1) if x%8 != 0]
   shuffle(ans)
   return ans

def PC_2_generator(size: int, n: int) -> List[int]:
    not_included = sample(range(size),n)
    arr = []
    for i in range(size):
        if(i not in not_included):
            arr.append(i+1)
    shuffle(arr)
    return arr
#initial permutation for plaintext.
def initial_permutation_generator(size: int) -> List[int]:
    a = [x for x in range(1,size+1)]
    shuffle(a)
    return a

def expansion_permutation_generator(size: int, n: int) -> List[int]:
   a = [x for x in range(1,size+1)]
   pos = sample(range(1,size+1),n)
   for i in pos:
     a.append(i)
   shuffle(a)
   return a

def permutation_generator(size: int) -> List[int]:
   a = [x for x in range(1,size+1)]
   shuffle(a)
   return a

def final_permutation_generator(size: int) -> List[int]:
   arr = [x for x in range(1,size+1)]
   shuffle(arr)
   return arr

def inverse_generator(arr: List[int]) -> List[int]:
   inv = [0 for i in range(len(arr))]
   for i,x in enumerate(arr):
     inv[x-1] = i+1 # Assuming numbers in the array start from 1
   return inv

def plaintext_preprocessor(plaintext: str, halfwidth: int =32) -> List[str]:
    length = 2*halfwidth
    x = len(plaintext)%length
    if(x != 0):
        x = length - x
    plaintext = '0'*x + plaintext
    # print(plaintext)
   # Make 2*halfwidth bit blocks of plaintext
    pt_arr = []
    i=0
    while(i+length <= len(plaintext)):
        pt_arr.append(plaintext[i:i+length])
        i += length
    return pt_arr


def key_preprocessor(key: str, halfwidth:int =32) -> str:
    if(len(key) > 2*halfwidth):
        key = key[:2*halfwidth]
    key = key.zfill(2*halfwidth)
    return key

#to generate 16 round key.
def round_keys_generator(key: str, rounds: int =16, half_width: int =32) -> Tuple[List[str], List[str]]:
    shift_by_table = [ 1, 1, 2, 2, 
                   2, 2, 2, 2, 
                   1, 2, 2, 2, 
                   2, 2, 2, 1 ]
    if(half_width == 32):    
        PC_1 = [ 57, 49, 41, 33, 25, 17, 9, 
             1, 58, 50, 42, 34, 26, 18, 
             10, 2, 59, 51, 43, 35, 27, 
             19, 11, 3, 60, 52, 44, 36, 
             63, 55, 47, 39, 31, 23, 15, 
             7, 62, 54, 46, 38, 30, 22, 
             14, 6, 61, 53, 45, 37, 29, 
             21, 13, 5, 28, 20, 12, 4 ]
     # Reduce keysize from 56 to 48 bits (Permuted Choice-2)
        PC_2 = [ 14, 17, 11, 24, 1, 5, 
             3, 28, 15, 6, 21, 10, 
             23, 19, 12, 4, 26, 8, 
             16, 7, 27, 20, 13, 2, 
             41, 52, 31, 37, 47, 55, 
             30, 40, 51, 45, 33, 48, 
             44, 49, 39, 56, 34, 53, 
             46, 42, 50, 36, 29, 32 ]
    else:
        PC_1 = PC_1_generator(2*half_width)
        PC_2 = PC_2_generator(len(PC_1), half_width//4)
       
   # Applying permuted choice-1 for dropping the parity bits in the key
    key = permutation(key, PC_1, len(PC_1))
   # Splitting 
    half = len(key)//2
    left = key[0:half]
    right = key[half:] 
    round_keys_hex = []     # RoundKeys in hexadecimal
    round_keys_binary = [] # RoundKeys in binary
    for i in range(rounds): 
     #  Shifting (take care of rounds)
        if(i < 16): # Use standard shifting table for upto 16th round
            left = shift_towards_left(left, shift_by_table[i])
            right = shift_towards_left(right, shift_by_table[i])
        else: # Use a shift of 1 for rounds more than 16
            left = shift_towards_left(left,1)
            right = shift_towards_left(right,1)

     # Combining 
        combined = left + right 

     # Key Compression 
        RoundKey = permutation(combined, PC_2, len(PC_2))
        round_keys_binary.append(RoundKey)
        RoundKey = bin_hex(RoundKey)
        round_keys_hex.append(RoundKey)
   
    return (round_keys_binary, round_keys_hex)


def s_box_value(val:int,row:int,col:int)->int:
    s_box = [
          [ 
            [ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
          ], 
          [ 
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
          ], 
          [ 
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
          ],
          [ 
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]
          ], 
          [ 
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
          ],
          [ 
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]
          ], 
          [ 
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]
          ],
          [ 
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 
          ]
      ] 
    return s_box[val][row][col]
  

def des_encryption(plaintext_arr: List[str], round_keys_binary: List[str], rounds: int =16, halfwidth: int =32) -> Tuple[str, List[str]]:
  
    if(halfwidth == 32):
        s_box_size = 8
    elif(halfwidth == 16):
        s_box_size = 4
    else:
        s_box_size = 16
    if(halfwidth == 32):
        initial_permutation = [ 58, 50, 42, 34, 26, 18, 10, 2, 
                  60, 52, 44, 36, 28, 20, 12, 4, 
                  62, 54, 46, 38, 30, 22, 14, 6, 
                  64, 56, 48, 40, 32, 24, 16, 8, 
                  57, 49, 41, 33, 25, 17, 9, 1, 
                  59, 51, 43, 35, 27, 19, 11, 3, 
                  61, 53, 45, 37, 29, 21, 13, 5, 
                  63, 55, 47, 39, 31, 23, 15, 7 ]
        expansion_permutation = [ 32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9, 
                8, 9, 10, 11, 12, 13, 
                12, 13, 14, 15, 16, 17, 
                16, 17, 18, 19, 20, 21, 
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1 ] 
        permutation_generated = [ 16, 7, 20, 21, 
                    29, 12, 28, 17, 
                    1, 15, 23, 26, 
                    5, 18, 31, 10, 
                    2, 8, 24, 14, 
                    32, 27, 3, 9, 
                    19, 13, 30, 6, 
                    22, 11, 4, 25 ]
        final_permutation = [ 40, 8, 48, 16, 56, 24, 64, 32, 
                39, 7, 47, 15, 55, 23, 63, 31, 
                38, 6, 46, 14, 54, 22, 62, 30, 
                37, 5, 45, 13, 53, 21, 61, 29, 
                36, 4, 44, 12, 52, 20, 60, 28, 
                35, 3, 43, 11, 51, 19, 59, 27, 
                34, 2, 42, 10, 50, 18, 58, 26, 
                33, 1, 41, 9, 49, 17, 57, 25 ]
        inv_initial_permutation = inverse_generator(initial_permutation)
    else:
        initial_permutation = initial_permutation_generator(2*halfwidth)
        expansion_permutation = expansion_permutation_generator(halfwidth,len(round_keys_binary[0]) - halfwidth)
        permutation_generated = permutation_generator(halfwidth)
        final_permutation = final_permutation_generator(2*halfwidth)
        inv_initial_permutation = inverse_generator(initial_permutation)

    final_ciphertext = ""
    round_ciphertexts = []
  
    for plaintext in plaintext_arr:
        plaintext = permutation(plaintext, initial_permutation, len(initial_permutation))

    for plaintext in plaintext_arr:
        left = plaintext[0:halfwidth]
        right = plaintext[halfwidth:]
        round_cipher = []
        for i in range(rounds): 
            right_expanded = permutation(right, expansion_permutation, len(expansion_permutation)) 
            x = XOR(round_keys_binary[i], right_expanded) 
            temp = ""
            for i in range(s_box_size):
                part = x[i*6:(i+1)*6]
                row = part[0] + part[5]
                row = int(row,2)
                col = part[1:-1]
                col = int(col,2)
                val = s_box_value(i%8,row,col) # mod 8 because of using same S-boxes circularly for a 64 bit halfwidth
                temp += bin(val)[2:].zfill(4)
      
      # Simple permutation
            temp = permutation(temp, permutation_generated, len(permutation_generated))

      # XOR of left and op 
            x = XOR(temp, left)
            left = x
      
      # Swaping at the end of each round
            if (i != rounds-1): # This ensures that we undo the swapping in the last round
                left, right = right, left
      
            round_cipher.append(str(left+right))
        round_ciphertexts.append(round_cipher)

    # Combine the halves
        combined = left + right
    # Final Permutation 
        ciphertext = permutation(combined, final_permutation, len(final_permutation))
        ciphertext = permutation(ciphertext, inv_initial_permutation, len(inv_initial_permutation))
        final_ciphertext += ciphertext

    final_ciphertext = bin_hex(final_ciphertext)
    return (final_ciphertext, round_ciphertexts)


