import tkinter as tk
from tkinter import ttk, messagebox

# Store contacts in a list of dictionaries
contacts = []

# --------- Functions ---------
def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for idx, contact in enumerate(contacts):
        contact_list.insert("", "end", iid=idx, values=(contact["name"], contact["phone"]))

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_var.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    clear_form()
    refresh_contacts()

def clear_form():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def on_select(event):
    selected = contact_list.focus()
    if selected:
        data = contacts[int(selected)]
        name_var.set(data["name"])
        phone_var.set(data["phone"])
        email_var.set(data["email"])
        address_var.set(data["address"])

def update_contact():
    selected = contact_list.focus()
    if selected:
        idx = int(selected)
        contacts[idx] = {
            "name": name_var.get(),
            "phone": phone_var.get(),
            "email": email_var.get(),
            "address": address_var.get()
        }
        refresh_contacts()
        clear_form()
    else:
        messagebox.showinfo("No Selection", "Select a contact to update.")

def delete_contact():
    selected = contact_list.focus()
    if selected:
        idx = int(selected)
        confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(idx)
            refresh_contacts()
            clear_form()
    else:
        messagebox.showinfo("No Selection", "Select a contact to delete.")

def search_contact():
    query = search_var.get().strip().lower()
    contact_list.delete(*contact_list.get_children())
    for idx, contact in enumerate(contacts):
        if query in contact["name"].lower() or query in contact["phone"]:
            contact_list.insert("", "end", iid=idx, values=(contact["name"], contact["phone"]))

# --------- UI Setup ---------
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("700x500")
root.configure(bg="#F0F8FF")

# ----- Styling -----
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 11), rowheight=25)
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("TButton", font=("Helvetica", 11))
style.configure("TLabel", font=("Helvetica", 11), background="#F0F8FF")
style.configure("TEntry", font=("Helvetica", 11))

# ----- Variables -----
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# ----- Entry Form -----
form_frame = tk.LabelFrame(root, text="Contact Details", bg="#F0F8FF", font=("Helvetica", 12, "bold"), padx=10, pady=10)
form_frame.pack(fill="x", padx=20, pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(form_frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Phone:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
tk.Entry(form_frame, textvariable=phone_var, width=30).grid(row=0, column=3, padx=5, pady=5)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(form_frame, textvariable=email_var, width=30).grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Address:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
tk.Entry(form_frame, textvariable=address_var, width=30).grid(row=1, column=3, padx=5, pady=5)

# ----- Buttons -----
btn_frame = tk.Frame(root, bg="#F0F8FF")
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="Update", command=update_contact).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="Delete", command=delete_contact).grid(row=0, column=2, padx=10)
ttk.Button(btn_frame, text="Clear", command=clear_form).grid(row=0, column=3, padx=10)

# ----- Search Bar -----
search_frame = tk.Frame(root, bg="#F0F8FF")
search_frame.pack(fill="x", padx=20)

tk.Label(search_frame, text="Search by Name or Phone:").pack(side="left", padx=5)
tk.Entry(search_frame, textvariable=search_var, width=30).pack(side="left", padx=5)
ttk.Button(search_frame, text="Search", command=search_contact).pack(side="left", padx=5)
ttk.Button(search_frame, text="Show All", command=refresh_contacts).pack(side="left", padx=5)

# ----- Contact List -----
list_frame = tk.Frame(root, bg="#F0F8FF")
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("Name", "Phone")
contact_list = ttk.Treeview(list_frame, columns=columns, show="headings")
contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone Number")
contact_list.pack(fill="both", expand=True)

contact_list.bind("<<TreeviewSelect>>", on_select)

# ----- Start -----
root.mainloop()
