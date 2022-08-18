def toggled(elem, st):
    cst = st.copy()
    if elem not in cst:
        cst.add(elem)
    elif elem in cst:
        cst.discard(elem)
    return cst

if __name__ == '__main__':
    READ_ONLY = 'read only'
    flags = set()
    new_flags = toggled(READ_ONLY, flags)
    print(READ_ONLY in flags)
    print(READ_ONLY in new_flags)
