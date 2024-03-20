def countwords():#function
    while True:
         st=input("enter  string:")
         if st.strip():#strip methods used to remove spaces
             st=st.rstrip()#rstrip remov es spaces in right side
             a=st.split(" ")#split used to split the string eith a specified character
             print(a)
             words=len(a)#length method is used to find the length of the string
             break
         else:#if user doesnot enter any string then it will ask the user to enter the string
             print("enter any string")
             continue
    return words
b=countwords()
print("number of words in given string:",b)

 
