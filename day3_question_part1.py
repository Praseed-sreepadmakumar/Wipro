def write_numbers_to_file(fname):
    try:
        with open(fname, 'r+') as file:
            for i in range(1,101):
                file.writelines(str(i) + " ")
    except Exception as e:
        return (f"An error occured: {e}")
    finally:
        file.close()
print(write_numbers_to_file("file1"))