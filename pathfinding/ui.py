import streamlit as st
import cv2
import numpy as np
import maze
import robocode

st.title('Maze Solver')
uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"])
opencv_image = None
marked_image = None

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

if opencv_image is not None:
    st.subheader('Use the sliders on the right to position the start and end points')
    start_x = st.sidebar.slider("Start X", value= 50, min_value=0, max_value=opencv_image.shape[1], key='sx')
    start_y = st.sidebar.slider("Start Y", value= 100, min_value=0, max_value=opencv_image.shape[0], key='sy')
    finish_x = st.sidebar.slider("Finish X", value= 100, min_value=0, max_value=opencv_image.shape[1], key='fx')
    finish_y = st.sidebar.slider("Finish Y", value= 100, min_value=0, max_value=opencv_image.shape[0], key='fy')
    marked_image = opencv_image.copy()
    circle_thickness=(marked_image.shape[0]+marked_image.shape[0])//2//100 #ui circle thickness based on img size
    cv2.circle(marked_image, (start_x, start_y), circle_thickness, (0,255,0),-1)
    cv2.circle(marked_image, (finish_x, finish_y), circle_thickness, (255,0,0),-1)
    st.image(marked_image, channels="RGB", width=800)

if marked_image is not None:
    if st.button('Solve Maze'):
        with st.spinner('Solving your maze'):
            path = maze.find_shortest_path(opencv_image,(start_x, start_y),(finish_x, finish_y))
        pathed_image = opencv_image.copy()
        path_thickness = (pathed_image.shape[0]+pathed_image.shape[0])//2//100
        maze.drawPath(pathed_image, path, 1)
        st.image(pathed_image, channels="RGB", width=800)
        print(path)
        maze.usepath(path)
#streamlit run c:/Users/aiw25/Downloads/pathfinding/ui.py 
#use the above code in terminal to run the full program, with whatever path is relevant for you