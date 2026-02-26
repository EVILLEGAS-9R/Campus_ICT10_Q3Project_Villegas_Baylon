from pyscript import display, document


def handle_signup(e):
    e.preventDefault()
    output_div = document.getElementById("signup-message")
    # Clear to prevent repeating messages
    output_div.innerHTML = ""
    display("Account created! You may now log in.", target="signup-message")

    document.getElementById("user_name").value = ""

def check_intramurals(e):
    output_div = document.getElementById("result")
    output_div.innerHTML = ""


    is_registered = document.getElementById("reg_yes").checked
    is_medical = document.getElementById("med_yes").checked
    grade = int(document.getElementById("grade").value)
    section = document.getElementById("section").value

    if not is_registered:
        display("Please complete the online registration.", target="result")
    elif not is_medical:
        display("Please secure a medical clearance.", target="result")
    elif grade < 7 or grade > 10:
        display("You are not eligible for Intramurals.", target="result")
    else:
    
        team = ""
        if grade == 7:
            team = "Blue Bears"
            img_file = "blue_bears.JPG.jpg"

        elif grade == 8:
            team = "Red Bulldogs"
            img_file = "red_bulldogs.JPG.jpg"
        elif grade == 9:
            team = "Yellow Tigers"
            img_file = "yellow_tigers.JPG.jpg"
        elif grade == 10:
           
            if section == "Ruby":
                team = "Blue Bears"
                img_file = "blue_bears.JPG.jpg"
            elif section == "Topaz":
                team = "Red Bulldogs"
                img_file = "red_bulldogs.JPG.jpg"

            elif section == "Sapphire":
                team = "Green Hornets"
                img_file = "green_hornets.JPG.jpg"
            elif section == "Emerald":
                team = "Yellow Tigers"
                img_file = "yellow_tigers.JPG.jpg"
        
        display("Congratulations! You are part of the " + team, target="result")


def display_players():
  
    classmates = [
        "Juan Dela Cruz", "Dylan Harper", "Victor Wenbanyama", 
        "Brook Lopez", "Mark Villanueva", "Dwight Ramos", 
        "Alpen Sengun", "Elena Smith", "Miguel Tan", "Lebron James"
    ]
    
    player_list_element = document.getElementById("playerList")
    
    if player_list_element:
        player_list_element.innerHTML = "" # Clear previous list
        
        
        for student in classmates:
            li = document.createElement("li")
            li.className = "list-group-item" 
            li.innerText = student
            player_list_element.appendChild(li)


if document.getElementById("playerList"):

    display_players()
