def ask_question(question):
    answer = input(f"{question} (yes/no): ").lower()
    return answer == "yes"

def diagnose_issue():
    potential_issues = []

    # Question 1
    if ask_question("Is your computer turning on?"):
        # Sub-questions for Question 1
        if not ask_question("Is the screen displaying anything?"):
            potential_issues.append("Display or graphics card issue.")
        if ask_question("Are there any unusual sounds coming from the computer?"):
            potential_issues.append("Hard drive or fan malfunction.")
    else:
        potential_issues.append("Power supply or motherboard failure.")

    # Question 2
    if not ask_question("Are peripherals (keyboard, mouse) working properly?"):
        if not ask_question("Is the keyboard functioning correctly?"):
            potential_issues.append("Keyboard driver or connection issue.")
        if not ask_question("Is the mouse working as expected?"):
            potential_issues.append("Mouse driver or connection issue.")

    # Question 3
    if ask_question("Have you recently installed new software or hardware?"):
        if ask_question("Is the new software causing any problems?"):
            potential_issues.append("Software compatibility issue.")
        if not ask_question("Is the new hardware properly installed?"):
            potential_issues.append("Hardware configuration issue.")

    # Question 4
    if ask_question("Is there a problem with internet connectivity?"):
        if ask_question("Is the connection wired?"):
            potential_issues.append("Network adapter or cable issue.")
        if not ask_question("Can other devices connect to the internet?"):
            potential_issues.append("Router or modem problem.")

    # Question 5
    if ask_question("Has there been a recent power outage or surge?"):
        if ask_question("Are other electronics affected by the power issue?"):
            potential_issues.append("Power supply or surge protector failure.")
        if ask_question("Did the computer shut down unexpectedly during the event?"):
            potential_issues.append("Power supply or motherboard issue.")

    # Question 6
    if ask_question("Is the computer running slowly or freezing frequently?"):
        if ask_question("Have you performed disk cleanup and defragmentation?"):
            potential_issues.append("Disk fragmentation or storage issue.")
        if  not ask_question("Is the antivirus software up to date?"):
            potential_issues.append("Malware or virus infection.")

    # Question 7
    if ask_question("Are there any error messages or pop-ups on the screen?"):
        if ask_question("Do the errors occur during specific tasks or programs?"):
            potential_issues.append("Software compatibility or corruption issue.")
        if ask_question("Have you recently updated the operating system?"):
            potential_issues.append("Operating system update or configuration issue.")
    
    # Question 8
    if ask_question("Is the computer making a loud noise during operation?"):
        if ask_question("Does the noise occur when performing specific tasks?"):
            potential_issues.append("Fan or cooling system malfunction.")
        if  not ask_question("Have you checked for dust buildup inside the computer?"):
            potential_issues.append("Dust accumulation or hardware overheating.")
            
    # Final potential issues
    if potential_issues:
        print()
        print()
        print("Potential issues detected:")
        for issue in potential_issues:
            print(f"- {issue}")
    else:
        print("No issues detected.")

# Usage
diagnose_issue()
