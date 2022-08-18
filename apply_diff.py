def apply_diff(st, df):
    if 'add' in df:
        st.update(df['add'])
    if 'remove' in df:
        st.difference_update(df['remove'])

if __name__ == '__main__':
    target = {'a','b'}
    diff = {'add': {'c'}, 'remove': {'a'}}
    apply_diff(target, diff)
    print(target == {'c', 'b'})
