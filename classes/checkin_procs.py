def validateCheckin(data: any):
    if data['badgeNumber'] is None or data['badgeNumber'] == '':
        return {
            "message": "No badge number was entered!",
            "status" : "error",
            "class"  : "text-danger",
            "received_data": data
        }

    return {
        "message": "Data received successfully!",
        "status": "success",
        "class": "text-success",
        "received_data": data
    }