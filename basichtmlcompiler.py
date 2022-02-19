def htmlchecker(filename):
    """ This is the function named html checker which will execute the whole program as the program is short """
    htmtags = {  # this dictionary will be used to check the html program or file for any invalid tag
        "</html>": "<html>",
        "</head>": "<head>",
        "</h>": "<h>",
        "</title>": "<title>",
        "</body>": "<body>",
        "</div>": "<div>",
        "</span>": "<span>",
        "</a>": "<a>",
        "</p>": "<p>",
        "</table>": "<table>",
        "</thead>": "<thead>",
        "</tbody>": "<tbody>",
        "</tr>": "<tr>",
        "</td>": "<td>",
        "</script>": "<script>",
        "</ul>": "<ul>",
        "</li>": "<li>",
        "</hr>": "<hr>",
        "</strong>": "<strong>",
        "</img>": "<img>"

    }
    html_file = open(filename)  # here open function is used to read the file that will be entered
    string_html_file = html_file.read()  # this is the original string file
    updatedfind = string_html_file.replace(' ', '')  # removing spaces in the string file to make it easy to be used
    findlist = updatedfind.split('>')
    updated_list = []
    opentags = []
    closetags = []
    empty_check = len(string_html_file)
    valid_file = 0  # initializing int to check if the inserted code is not string or other
    for lists in findlist:
        new_list_item = lists + '>'  # adding ">" to each string in the list findlist as the findlist original delete ">" in split
        updated_list.append(new_list_item)  # adding the new list items in new updated list
    updated_list.pop()
    for lists in updated_list:  # for loop for checking if there is a string inside specific tags like <a>,<p>,
        # <meta> and <html>
        if "<p" in lists or "<p1" in lists or "<p2" in lists or "<p3" in lists or "<p4" in lists:
            replace_with = "<p>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)
        elif "</p" in lists or "</p1" in lists or "</p2" in lists or "</p3" in lists or "</p4" in lists:
            replace_with = "</p>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)

        elif "<h1" in lists or "<h2" in lists or "<h3" in lists or "<h4" in lists:
            replace_with = "<h>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)
        elif "</h1" in lists or "</h2" in lists or "</h3" in lists or "</h4" in lists:
            replace_with = "</h>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)
        elif "<a" in lists:
            replace_with = "<a>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)
        elif "<meta" in lists:

            replace_with = "<meta>"
            updated_list.insert(updated_list.index(lists), replace_with)
            updated_list.remove(lists)
        elif "<html" in lists and len(lists) > 6:
            replace = "<html>"
            updated_list.insert(updated_list.index(lists), replace)
            updated_list.remove(lists)
    for list_iterat in range(
            len(updated_list)):  # for loop to check if the tags are closed with appropriate corresponding tags
        if "<" in updated_list[list_iterat] and "<" in updated_list[list_iterat]:

            initial_index_of_tags = updated_list[list_iterat].index("<")
            final_index_of_tags = updated_list[list_iterat].index(">")
            # slicing tags using appropriate index
            tag = str(updated_list[list_iterat][initial_index_of_tags:final_index_of_tags + 1])
            # if statement to check the tag is a tag which doesn't have closing tag
            if tag == "<!DOCTYPEhtml>" or tag == "<br>" or tag == "<meta>":
                continue
            if tag not in htmtags:
                opentags.append(tag)
            elif tag in htmtags:
                closetags.append(tag)
                if len(opentags) != 0:
                    valid_file = 1
                    if htmtags[tag] == opentags[-1]:
                        opentags.pop()
                        closetags.pop()
    if len(opentags) == 0 and len(closetags) == 0 and empty_check != 0 and valid_file == 1:
        print("This file is valid")
    else:
        print("This file is not valid")


htmlchecker("ha.html")
