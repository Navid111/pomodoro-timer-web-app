import time
import streamlit as st

# Initialize session state variables
if "is_running" not in st.session_state:
    st.session_state.is_running = False

if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 0

st.title("Pomodoro Timer")
st.write("A simple focus timer built with Streamlit.")

# Input for Pomodoro duration
pomodoro_duration = st.number_input("Set Pomodoro duration (minutes)", min_value=1, max_value=120, value=25)

# Total time in seconds
total_seconds = pomodoro_duration * 60

col1, col2, col3 = st.columns(3)
with col1:
    start_button = st.button("Start / Resume")
with col2:
    pause_button = st.button("Pause")
with col3:
    reset_button = st.button("Reset")

# Timer controls
if start_button:
    st.session_state.is_running = True
    if st.session_state.remaining_time == 0:  # Start fresh
        st.session_state.remaining_time = total_seconds
elif pause_button:
    st.session_state.is_running = False
elif reset_button:
    st.session_state.is_running = False
    st.session_state.remaining_time = 0

# Timer display
timer_container = st.empty()

# Countdown logic
while st.session_state.is_running and st.session_state.remaining_time > 0:
    minutes_left = int(st.session_state.remaining_time // 60)
    seconds_left = int(st.session_state.remaining_time % 60)
    
    # Display the remaining time
    timer_container.metric("Time Remaining", f"{minutes_left:02d}:{seconds_left:02d}")
    
    # Wait for 1 second and update the timer
    time.sleep(1)
    st.session_state.remaining_time -= 1

# When the timer ends
if st.session_state.remaining_time == 0 and st.session_state.is_running:
    st.success("Time is up!")
    st.balloons()
    st.session_state.is_running = False
