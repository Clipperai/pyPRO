import streamlit as st # type: ignore

st.title("Contact Book Saver")



if "contacts" not in st.session_state:
     st.session_state.contacts = {}



choice= st.selectbox("Select:", ["-select-","Add Contacts", "View Contacts", "Search Contacts"])

button = st.button("Submit")

if button:

        if choice == 'Add Contacts':
            with st.form("form"):

                name = st.text_input("Enter name: ").lower().strip()
                phone = st.text_input("Enter phone: ").strip()

                submitted = st.form_submit_button("Add")

                if submitted:
                    
                    if name and phone:

                        st.session_state.contacts[name] = phone
                        st.toast("done")
                        st.success("Contact Added successfully")
                    
                    else:
                        st.toast("Enter Details first!")
                

        elif choice == 'View Contacts':  
            if st.button("View"):  
                   
                if st.session_state.contacts:
                    st.success("Saved Contacts: ")
                    st.success(st.session_state.contacts)
                    # for n,p in contacts:
                    #     st.write(f"{n,p}")
                
                else:

                    st.error("Not any Contacts here yet. ")
                    

        elif choice == 'Search Contacts':       
                
                name = st.text_input("Enter name to search: ").lower().strip()
                if st.button("Search"):
                    if name in st.session_state.contacts.items():
                        st.success("Yes")
                        st.success(f"Number: {st.session_state.contacts[name]}")
                    
                    else:

                        st.error("Contact not found")   
                
            
        else:
                st.error("Invalid choice")
                st.toast("Select a Specific Operation first!")
            
                    
                    

            