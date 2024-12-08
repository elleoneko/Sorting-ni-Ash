from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st
import time
import customtkinter as ctk

selected_button = None

def set_algo(algo, button):
    global selected_button
    global chosen_algo

    chosen_algo = algo

    if selected_button is not None:
        reset_button(selected_button)
    button.configure(fg_color=("#7c3aed","#9f7aea"))
    selected_button = button
    

def reset_button(button):
    button.configure(fg_color=("white","#020024"))

def steps(message):
    process_text_area.insert(END, message + "\n")
    process_text_area.yview(END)  # Scroll to the end
    process_text_area.update()
    time.sleep(0.1) # PALITAN PARA BUMILIS YUNG PRINT

def submit():
    numbers = input_num.get()
    entered_numbers_box.configure(state="normal")
    # Clear the previous output
    entered_numbers_box.delete(1.0, END)
    entered_numbers_box.insert(END, f"Inputted Numbers: \n {numbers}")
    entered_numbers_box.configure(state="disabled")

def sort():
    process_text_area.delete(1.0, END)
    processed_text_area.delete(1.0, END)
    numbers = input_num.get()
    if chosen_algo == "bubble sort":
        print(chosen_algo)
        bubbleSort(convert_to_list(numbers))
    elif chosen_algo == "insertion sort":
        print(chosen_algo)
        insertionSort(convert_to_list(numbers))
    elif chosen_algo == "selection sort":
        print(chosen_algo)
        selectionSort(convert_to_list(numbers))
    elif chosen_algo == "merge sort":
        print(chosen_algo)
        mergeSort(convert_to_list(numbers))
    elif chosen_algo == "shell sort":
        print(chosen_algo)
        shellSort(convert_to_list(numbers))
    else:
        pass  
def bubbleSort(myList):

    # Bubble Sort algorithm
    for i in range(len(myList)):
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
            steps(f"Sorting: {myList}")
    processed_text_area.insert(END, f"Bubble Sorted List: {myList}")
    return myList

def insertionSort(myList):
    # Insertion Sort algorithm
    for i in range(1, len(myList)):
        curNum = myList[i]
        j = i - 1
        while j >= 0 and myList[j] > curNum:
            myList[j + 1] = myList[j]
            j -= 1
        myList[j + 1] = curNum
        steps(f"Step {i}: {myList}")
    processed_text_area.insert(END, f"Insertion Sorted List: {myList}")
    return myList

def selectionSort(myList):
    # Selection Sort algorithm
    for i in range(0, len(myList) - 1):
        minValue = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[minValue]:  # Find the smallest value
                minValue = j
        if minValue != i:  # Swap only if a smaller value is found
            myList[i], myList[minValue] = myList[minValue], myList[i]
        steps(f"Step {i+1}:{myList}\n")
    processed_text_area.insert(END, myList)
    return myList

def mergeSort(myList, new_list=None):
    if new_list is None:
            new_list = myList

    if len(new_list) > 1:
        mid = len(new_list) // 2
        L = new_list[:mid]
        R = new_list[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                new_list[k] = L[i]
                i += 1
            else:
                new_list[k] = R[j]
                j += 1
            k += 1
            steps(f"Merging: {new_list}")

        while i < len(L):
            new_list[k] = L[i]
            i += 1
            k += 1
            steps(f"Merging: {new_list}")

        while j < len(R):
            new_list[k] = R[j]
            j += 1
            k += 1
            steps(f"Merging: {new_list}")

    processed_text_area.delete(1.0,END)
    processed_text_area.insert(END, f"Sorted List: {new_list}")
    return new_list

def shellSort(myList):

    n = len(myList)
    gap = n // 2  # Start with a large gap and reduce it over time

    # Perform a gap-based insertion sort
    while gap > 0: 
        steps(f"Gap: {gap}")  # Show the current gap
        for i in range(gap, n):
            temp = myList[i]
            j = i

            # Perform the gap-based insertion
            while j >= gap and myList[j - gap] > temp:
                steps(f"Swapping {myList[j]} and {myList[j - gap]}")
                myList[j] = myList[j - gap]
                j -= gap
            myList[j] = temp
        process_text_area.insert(END, f"List after gap {gap}: {myList}\n")
        
        gap //= 2  # Reduce the gap for the next pass
    
    processed_text_area.insert(END, f"Shell Sorted List: {myList}")

# lagay yung input numbers sa list
def convert_to_list(input_num):
    try:
        new_list = [int(item.strip()) for item in input_num.split()]
        return new_list
    except ValueError:
        print("not a number")

def toggle_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Light" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)

    if new_mode == "Light":
        toggle_button.configure(image= PhotoImage(file="./light.png"))
    else:
        toggle_button.configure(image= PhotoImage(file="./dark.png"))

# WINDOW
window = ctk.CTk(fg_color=("#fbfbfe","#010104"))
window.geometry('1024x750')
window.title("GUI Sorting Algorithms")

# LIGHT DARK MODE
toggle_button = ctk.CTkButton(window, 
                              text="Light/Dark",
                              image=PhotoImage(file="./light.png"), command=toggle_mode,
                              bg_color=("white","#010104"),
                            border_color=("white","#010104"),
                            hover_color=("#a78bfa","#9f7aea"),
                            fg_color=("#7c3aed","#020024"),
                            text_color=("#202020","#e0e0e0"),
                            font=("Poppins", 16))
toggle_button.pack(pady=5)

sort_alg_label = ctk.CTkLabel(window, 
                              text="Sorting Algorithms",
                              font=("Poppins", 24,"bold")).pack()
num_sort_label = ctk.CTkLabel(window, 
                              text="Enter numbers to be sorted separated by space:",
                              font=("Poppins", 16)).pack()


# Create a frame to hold the Entry and Button
enter_num_frame = ctk.CTkFrame(window,
                               fg_color=("white","#010104"))
enter_num_frame.pack(pady=5)

input_num = ctk.CTkEntry(enter_num_frame, 
                         width=350, 
                         height=50, 
                         corner_radius=8,
                         fg_color=("white","#020024"),
                         text_color=("#202020","#e0e0e0"),
                         bg_color=("white","#020024"),
                         font=("Poppins", 16))
input_num.pack(side='left')

submit_button = ctk.CTkButton(enter_num_frame, text="Submit", command=submit,
                              bg_color=("white","#010104"),
                              corner_radius=8,
                            border_color=("white","#020024"),
                            hover_color=("#a78bfa","#9f7aea"),
                            fg_color=("#7c3aed","#020024"),
                            text_color=("#202020","#e0e0e0"),
                            font=("Poppins", 16))
submit_button.pack(side='left', padx=5)


entered_numbers_box = ctk.CTkTextbox(window,wrap='word',width=300,height=50)
entered_numbers_box.pack()
entered_numbers_box.configure(state="disabled")

ctk.CTkLabel(window, text="Select Sorting Algorithm:",
             font=("Poppins", 16)).pack()

hover_message = ctk.CTkLabel(window, text="", width=200, height=40)
hover_message.pack(pady=20)

def on_hover(event, message):
    hover_message.configure(text=message)

# Function to clear the message when mouse leaves the button
def on_leave(event):
    hover_message.configure(text="") 



# Create buttons for sorting algorithms
button_frame = ctk.CTkFrame(window, fg_color="transparent")
button_frame.pack()

bubble_sort_btn= ctk.CTkButton(button_frame,text="Bubble Sort",
              width=380,
              height=30,
              corner_radius=8,
              border_width=2,
              border_color=("#7c3aed","#020024"),
              hover_color=("#7c3aed","#9f7aea"),
              fg_color=("white","#020024"),
              text_color=("#202020","#e0e0e0"),
              command=lambda: set_algo("bubble sort",bubble_sort_btn),
              font=("Poppins", 16))
bubble_sort_btn.pack(pady=3)

bubble_sort_btn.bind("<Enter>", lambda event: on_hover(event, "Bubble Sort is blah blah."))
bubble_sort_btn.bind("<Leave>", lambda event: on_leave)

insertion_sort_btn= ctk.CTkButton(button_frame,text="Insertion Sort",
              width=380,
              height=30,
              corner_radius=8,
              border_width=2,
              border_color=("#7c3aed","#020024"),
              hover_color=("#7c3aed","#9f7aea"),
              fg_color=("white","#020024"),
              text_color=("#202020","#e0e0e0"),
              command=lambda: set_algo("insertion sort",insertion_sort_btn),
              font=("Poppins", 16))
insertion_sort_btn.pack(pady=3)

insertion_sort_btn.bind("<Enter>", lambda event: on_hover(event, "Insertion Sort is blah blah."))
insertion_sort_btn.bind("<Leave>", lambda event: on_leave)

selection_sort_btn= ctk.CTkButton(button_frame,text="Selection Sort",
              width=380,
              height=30,
              corner_radius=8,
              border_width=2,
              border_color=("#7c3aed","#020024"),
              hover_color=("#7c3aed","#9f7aea"),
              fg_color=("white","#020024"),
              text_color=("#202020","#e0e0e0"),
              command=lambda: set_algo("selection sort",selection_sort_btn),
              font=("Poppins", 16))
selection_sort_btn.pack(pady=3)

selection_sort_btn.bind("<Enter>", lambda event: on_hover(event, "Selection Sort is blah blah."))
selection_sort_btn.bind("<Leave>", lambda event: on_leave)

merge_sort_btn= ctk.CTkButton(button_frame,text="Merge Sort",
              width=380,
              height=30,
              corner_radius=8,
              border_width=2,
              border_color=("#7c3aed","#020024"),
              hover_color=("#7c3aed","#9f7aea"),
              fg_color=("white","#020024"),
              text_color=("#202020","#e0e0e0"),
              command=lambda: set_algo("merge sort", merge_sort_btn),
              font=("Poppins", 16))
merge_sort_btn.pack(pady=3)

merge_sort_btn.bind("<Enter>", lambda event: on_hover(event, "Merge Sort is blah blah."))
merge_sort_btn.bind("<Leave>", lambda event: on_leave)

shell_sort_btn= ctk.CTkButton(button_frame,text="Shell Sort",
              width=380,
              height=30,
              corner_radius=8,
              border_width=2,
              border_color=("#7c3aed","#020024"),
              hover_color=("#7c3aed","#9f7aea"),
              fg_color=("white","#020024"),
              text_color=("#202020","#e0e0e0"),
              command=lambda: set_algo("shell sort", shell_sort_btn),
              font=("Poppins", 16))
shell_sort_btn.pack(pady=3)

shell_sort_btn.bind("<Enter>", lambda event: on_hover(event, "Shell Sort is blah blah."))
shell_sort_btn.bind("<Leave>", lambda event: on_leave)

sort_button = ctk.CTkButton(button_frame, text="Sort",
                            border_width=2,
              border_color=("white","#020024"),
              fg_color=("#7c3aed","#020024"),
              text_color=("#202020","#e0e0e0"),
              hover_color=("#a78bfa","#9f7aea"),
              font=("Poppins", 16),
              command=sort).pack(pady=3)

process_frame = ctk.CTkFrame(window,fg_color='transparent')
process_frame.pack(fill=None,padx=50,pady=10)

process_text_area = ctk.CTkTextbox(process_frame,wrap='word',width=300,height=200)
process_text_area.pack(side="left", fill="both", expand=True)

processed_text_area = ctk.CTkTextbox(process_frame,wrap='word',width=300,height=200)
processed_text_area.pack(side="left", fill="both", expand=True,padx=10)

#process_text_area.configure(state="disabled")
#processed_text_area.configure(state="disabled")

window.resizable(False, False)
window.mainloop()