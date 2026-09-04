print ("================")
print ("Welcome here")
print ("My first post!")
print ("================")

username = "cool_creator"
bio = "Fun Blogger"
followers = 1

print (username, "username")
print (bio, "bio")
print (followers, "followers")

followers += 50
print ("Day 1 followers", followers)

followers += 100
print ("Day 2 followers", followers)

followers += 189
print ("Day 3 followers", followers)

username = input("Enter Username: ")
age = int(input("Enter age: "))
category = input("Enter Content Category: ")

print("\n Instagram Profile")
print("=====================")
print("Username:", username)
print("Age: ", age)
print("Category: ", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")