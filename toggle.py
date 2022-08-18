def toggle(elem, st):
    if elem not in st:
        st.add(elem)
    elif elem in st:
        st.discard(elem)

if __name__ == '__main__':
    READ_ONLY = 'read only'
    flags = set()
    toggle(READ_ONLY, flags)
    print(READ_ONLY in flags)
    toggle(READ_ONLY, flags)
    print(READ_ONLY in flags)
