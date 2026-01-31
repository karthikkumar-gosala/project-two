id = input("Enter your Student id")
email = input("Enter your Email")
password = input("Enter your Password")
ref = input("Enter your refaral code :")
val1=len(id)
val2=len(email)
val3=len(password)
val4=len(ref)
if (id[0] == 'C' and id[1] == 'S' and id[2] == 'E' and id[3] == '-' and id[val1-1].isdigit() and id[val1-2].isdigit() and id[val1-3].isdigit()) :

    if (email.count('@') == 1 and email.count('.') == 1 and email[0] != '@' and email[-1] != '@' and '.' in email and
        ' ' not in email and '#'  not in email and '$' not in email  and '%' not in email and '&' not in email and '!' not in email and
        '*' not in email  and '*' not in email and email[val2-1] == 'u' and email[val2-2] == 'd' and email[val2-3] == 'e' and email[val2-4] == '.'):

         if (val3>=8 and password[0].isupper() and any(ch.isdigit() for ch in password)) :

              if (ref[0]=='R' and ref[1] == 'E' and ref[2] == 'F' and ref[val4-1] == '@'and sum(ch.isdigit() for ch in password)>=2) :
                  print("Approved")
              else :
                  print("Rejected 4")
         else:
                print("Rejected 3")
    else:
        print("Rejected 2")
else:
        print("Rejected 1")

