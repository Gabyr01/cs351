import tkinter as tk
# This will keep track of the current line being read
current_line_index = 0
# Method to handle action on clicking Next button
def next_line():
    global current_line_index
    # Getting the text from the input side
    text = ip_text_box.get('1.0', 'end-1c').split('\n')
    #if the current line index is out of range of text length
    if current_line_index >= len(text) - 1:
        return
    # cleaning the current line text box
    ip_line_tb.delete(0, tk.END)
    # inserting the current line value
    ip_line_tb.insert(tk.END, current_line_index + 1)
    # inserting the next line output side
    op_text_box.insert(tk.END, text[current_line_index] + '\n')
    current_line_index += 1
    # handling the action on cicking quit button
def quit():
    # closes the app
    app.quit()
    
# Main window
app = tk.Tk()
app.title('Lexical Analyzer for TinyPie')
app.geometry("1500x700+20+50")
app.resizable(False, False)
# Input side widgets and their places
ip_container = tk.Frame(app, width=1, height=1)
ip_container.grid_propagate(False)
ip_container.pack(side="left", fill="both", expand=True)
ip_label = tk.Label(app, text='Source Code Input:')
ip_label.place(x=50, y=50)
ip_text_box = tk.Text(ip_container)
ip_text_box.place(x=50, y=80)
ip_line_label = tk.Label(app, text='Current Processing Line:')
ip_line_label.place(x=400, y=500)
ip_line_tb = tk.Entry(app)
ip_line_tb.size()
ip_line_tb.place(x=550, y=500)
ip_next_button = tk.Button(app, text='Next', command=next_line)
ip_next_button.place(x=550, y=550)
# Output side widgets and their places

op_container = tk.Frame(app, width=10, height=10)
op_container.grid_propagate(False)
op_container.pack(side="right", fill="both", expand=True)
op_label = tk.Label(app, text='Lexical Analysed Result:')
op_label.place(x=790, y=50)
op_text_box = tk.Text(op_container)
op_text_box.place(x=50,y=80)
op_next_button = tk.Button(app, text='Quit', command=quit)
op_next_button.place(x=1350, y=550)

# Executing the app to launch it
app.mainloop()