#lists for storing words and dictionaries for count of words and characters
user1_chat=[]
user2_chat=[]
char_count={}
word_count={}
#length of conversation
conversation_length=0
print("----------------------Welcome to chat box---------------------------")
while(1):
    print("Press A Send message to send as User1")
    print("Press B Send message to send as User2")
    print("Enter quit to end chat")
    #getting user
    user=input()
    if user=='A':
        print("Enter the message:")
        #getting message
        message=input().split()
        #adding words to list
        user1_chat.extend(message)
        #incrementing conversation size
        conversation_length+=1
    elif user=='B':
        print("Enter the message:")
        #getting message
        message=input().split()
        #adding words to list
        user2_chat.extend(message)
        #incrementing conversation size
        conversation_length+=1
    #for exiting chat
    elif user.lower()=='quit':
        break
    #for undefined behaviour
    else:
        print("Please enter the valid input")
#calculating word and character counts of user 1
for i in user1_chat:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
    char_list=list(i)
    for i in char_list:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
#calculating word and character counts of user 2
for i in user2_chat:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
    char_list=list(i)
    for i in char_list:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
print("Enter 1 to view the number of repetition of a character")
print("Enter 2 to view the number of repetition of a word")
print("Enter 3 to view the conversation length")
while(1):
    value=int(input())
    if value==1:
        print("Displaying character count")
        if(len(char_count)==0):
            print("No characters")
            break
        for i in char_count:
            print(i,"and its count is:",char_count[i])
        print("Exiting app")
        break
    elif value==2:
        if(len(word_count)==0):
            print("No words")
            break
        print("Displaying word count")
        for i in word_count:
            print(i,"and its count is:",word_count[i])
        print("Exiting app")
        break
    elif value==3:
        print("Displaying conversation length")
        print("Conversation length:",conversation_length)
        print("Exiting app")
        break
    else:
        print("Please enter valid number")
'''
input:
A
hi
B
hello
A
how are you
B
fine
quit
1
'''


    
