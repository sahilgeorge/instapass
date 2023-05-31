import instaloader
import re




print("INSTAPASS VER 0.0.1")
print("By sahilgeorge2007")



# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
uuid = input("Enter your username(as in instagram): ")
pwd = input("\nEnter your instagram passsword: ")


bot.login(uuid, pwd)

print("\nLogin Successful!\n")


uid = input("Enter the username to search: ")

# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, uid)

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)






#printing a bunch of stuff

print(profile)
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
print("Emails extracted from the bio:", emails)





