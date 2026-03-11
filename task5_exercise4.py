import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Store Management System")

tab1, tab2, tab3 = st.tabs(["Add Item", "Browse Items", "Statistics"])

# Tab 1: Form to add items
with tab1:
    with st.form("item_form"):
        item_id = st.number_input("ID", min_value=1, step=1)
        name = st.text_input("Item Name")
        price = st.number_input("Price", min_value=0.01)
        quantity = st.number_input("Quantity", min_value=0, step=1)
        category = st.selectbox("Category", ["Electronics", "Groceries", "Clothing", "Other"])
        
        submitted = st.form_submit_button("Add Item")
        if submitted:
            payload = {"id": item_id, "name": name, "price": price, "quantity": quantity, "category": category}
            response = requests.post(f"{BASE_URL}/items", json=payload)
            if response.status_code == 200:
                st.success("Item added successfully!")
            else:
                st.error(f"Error: {response.json().get('detail')}")

# Tab 2: Browse and Filter
with tab2:
    col1, col2 = st.columns(2)
    cat_filter = col1.text_input("Filter by Category")
    price_filter = col2.number_input("Max Price Filter", min_value=0.0)
    
    params = {}
    if cat_filter: params["category"] = cat_filter
    if price_filter > 0: params["max_price"] = price_filter
    
    res = requests.get(f"{BASE_URL}/items", params=params)
    if res.status_code == 200:
        st.table(res.json())

# Tab 3: Statistics
with tab3:
    res = requests.get(f"{BASE_URL}/stats")
    if res.status_code == 200:
        stats = res.json()
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Items", stats["total_items"])
        c2.metric("Total Inventory Value", f"FCFA{stats['total_value']:.2f}")
        c3.metric("Most Expensive", stats["most_expensive"])