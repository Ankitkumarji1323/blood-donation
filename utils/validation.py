def validate_donor_data(attrs):
    if "first_name" in attrs and len(attrs.get("first_name")) < 1:
        return "First name field is required"
    elif "last_name" in attrs and len(attrs["last_name"]) < 1:
        return "Last name field is required"
    elif "address" in attrs and len(attrs["address"]) < 5:
        return "Enter address field is required"
    else:
        return "Please provide valid options"
