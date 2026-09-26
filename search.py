def search_plate(plate: str) -> str:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError

    url = f"https://www.nummerplade.net/nummerplade/{plate}.html"

    req = Request(url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }   
    )

    try:
        html = urlopen(req).read().decode("utf-8")
    except (HTTPError, URLError) as e:
        print(f"Error {e}")
        return None

    data = find_data("title", html)
    return data


def find_data(h_type: str, html):
    import re

    header = f"<{h_type}.*?>.*?</{h_type}>"
    results_header = re.search(header, html, re.IGNORECASE)
    if results_header:
        return re.sub("<.*?>", "", results_header.group())
    return "Header not found"


def check_plate(plate: str) -> str:
    import re
    parsed_plate = re.sub(r'[^a-zA-Z0-9]','', plate)
    plate_format = ["a","a","n","n","n","n","n"]
    
    if len(parsed_plate) != len(plate_format):
        return None

    for i, char in enumerate(parsed_plate):
        if not (plate_format[i] == "a" and char.isalpha() or plate_format[i] == "n" and char.isnumeric()):
            return None
    
    return parsed_plate


def test(plate) -> str:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError

    url = f"https://www.nummerplade.net/nummerplade/{plate}.html"
    req = Request(url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }   
    )

    
    try:
        html = urlopen(req).read().decode("utf-8")
    except (HTTPError, URLError) as e:
        print(f"Error {e}") 
    return html


if __name__ == "__main__":
    print(search_plate("ea57302"))
    print(check_plate("ET #àáâ96 00 6,!"))