def verify_binary(preorder):
    n=len(preorder)
    i=0
    st=[]
    while i<n:
        while len(st)>2 and st[-1]=='#' and st[-2]=='#':
            st.pop()
            st.pop()
            if st[-1]=='#':return False
            st.pop()
            st.append('#')

        st.append(preorder[i])
        i+=1

    while len(st)>2 and st[-1]=='#' and st[-2]=='#':
            st.pop()
            st.pop()
            st.pop()
            st.append('#')

    if len(st)==1 and st[-1]=='#':
        return True

    return False


check1="9,3,4,#,#,1,#,#,2,#,6,#,#"
check1.split(',')
check2="1,#"
print verify_binary(check1.split(','))

