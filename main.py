import streamlit as st
import numpy as np
import pandas as pd

st.title("Eigen vectors and its application in google page rank algorithm")
st.markdown("--------")
st.header("The below program is a scaled down attempt to stimulate the original google page ranks algorithm")
st.subheader("In this project, lets try imagining a small version of the internet with only 4 websites...")
st.subheader("every website here connects to all others exept itself....")
st.markdown("--------")
a=st.button("Wikipedia.org")
b=st.button("Instagram")
c=st.button("Facebook")
d=st.button("firefox")
st.markdown("--------")
st.subheader("Here the first task of the page ranker algorithm is to collect a history of your browsing data....based on the order of your clicks, it calculates all the websites you visited and the order in which you did...")

clickH=[]
if "clickH" not in st.session_state:
    st.session_state.clickH=[]
if a:
    st.session_state.clickH.append("A")
if b:
    st.session_state.clickH.append("B")
if c:
    st.session_state.clickH.append("C")
if d:
    st.session_state.clickH.append("D") 
st.markdown("-------")   
st.text(st.session_state.clickH)
st.markdown("-------")
st.subheader("next it puts your data into a matrix A :")

click=st.session_state.clickH
picks=["A","B","C","D"]
n=len(picks)
matrix=np.zeros((n,n),dtype=int)
matrix=np.array(matrix)
for i in range(len(click)-1):
    first=click[i]
    next=click[i+1]
    row=picks.index(first)
    coll=picks.index(next)
    matrix[row][coll]+=1
matrix_str = [[str(val) for val in row] for row in matrix]
latex_rows = []
for label, row in zip(picks, matrix_str):
    latex_rows.append(label + " & " + " & ".join(row))
latex_matrix = r"\begin{bmatrix}" + r" \\ ".join(latex_rows) + r"\end{bmatrix}"
st.latex(latex_matrix)
st.markdown("-------")


st.header("to get the initial matrix we apply the formula:")

st.latex(r'''
R_i = \frac{1-d}{N} + dA_i
''')

st.subheader("where...")
st.text("d : damping factor")
st.text("N : total websites present")
st.markdown("-----")


st.subheader("by normalizing and dampning the matrix we get out initial vector...")


nolinks= np.count_nonzero(matrix, axis=1)
#st.write(nolinks)
ra1=0.85*((matrix[0][0])/nolinks[0])+(0.15/4)
ra2=0.85*((matrix[0][1])/nolinks[0])+(0.15/4)
ra3=0.85*((matrix[0][2])/nolinks[0])+(0.15/4)
ra4=0.85*((matrix[0][3])/nolinks[0])+(0.15/4)
rb1=0.85*((matrix[1][0])/nolinks[1])+(0.15/4)
rb2=0.85*((matrix[1][1])/nolinks[1])+(0.15/4)
rb3=0.85*((matrix[1][2])/nolinks[1])+(0.15/4)
rb4=0.85*((matrix[1][3])/nolinks[1])+(0.15/4)
rc1=0.85*((matrix[2][0])/nolinks[2])+(0.15/4)
rc2=0.85*((matrix[2][1])/nolinks[2])+(0.15/4)
rc3=0.85*((matrix[2][2])/nolinks[2])+(0.15/4)
rc4=0.85*((matrix[2][3])/nolinks[2])+(0.15/4)
rd1=0.85*((matrix[3][0])/nolinks[3])+(0.15/4)
rd2=0.85*((matrix[3][1])/nolinks[3])+(0.15/4)
rd3=0.85*((matrix[3][2])/nolinks[3])+(0.15/4)
rd4=0.85*((matrix[3][3])/nolinks[3])+(0.15/4)

initialmat=((ra1,ra2,ra3,ra4),(rb1,rb2,rb3,rb4),(rc1,rc2,rc3,rc4),(rd1,rd2,rd3,rd4))
initialmat=np.array(initialmat)
im=pd.DataFrame(initialmat)
latex_rows = []
for row in initialmat:
    row_str = " & ".join([f"{val:.4f}" for val in row])  # format to 4 decimals
    latex_rows.append(row_str)

mlatex = r"\begin{bmatrix}" + r" \\ ".join(latex_rows) + r"\end{bmatrix}"
st.subheader("A :")
st.latex(mlatex)
st.markdown("----")
st.subheader("Let the initial vector be V :")
initialvect=(0.25,0.25,0.25,0.25)
initialvect=np.array(initialvect)
v=initialvect.copy()
vect_latex = r"\begin{bmatrix}" + " & ".join(map(str,v)) + r"\end{bmatrix}"
st.latex(vect_latex)
st.text("since the number of websites are 4 and the chances you click one of the websites is 1/4")
st.markdown("-----")
st.subheader("now we get a matrix and an initial vector....all we need to do is apply the matrix transformation on the vector for a few times to get a vector with stable values and where lamda is 1")
st.latex(r"A^T \, v = \lambda \, v")
st.markdown("---")
st.header("finally after 10 iterations we get our dominant eigen vector..")
for i in range (10):
    v=initialmat.T@v
    v = v / np.sum(v)
vect_latex = r"\begin{bmatrix}" + " & ".join(f"{x:.4f}" for x in v) + r"\end{bmatrix}"    
st.latex(vect_latex)
st.subheader("--------------------------------------------------------------------")
st.subheader("the bar grapgh below represents the final vector and the website with the highest value is the most popular or most frequented page")
st.header("  ")
st.bar_chart(v)
st.subheader("--------------------------------------------------------------------")
st.subheader("the challenges....")
st.subheader(" Scalability...Dangling nodes....Convergence time ")
st.subheader("--------------------------------------------------------------------")
st.subheader("The applications....")
st.subheader(" page recommendations...social networking app....academic research ")