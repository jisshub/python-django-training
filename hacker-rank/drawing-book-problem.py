count = 0
current_page = 1


def drawing_books(final_page):
    global count, current_page
    while current_page < final_page - 1:
        count += 1
        if final_page - current_page > 1:
            # count += 1
            current_page += 1
        elif final_page - current_page is 1:
            current_page += 1

    return count


print(drawing_books(2))
