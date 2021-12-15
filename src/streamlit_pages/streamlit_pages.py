# -*- coding: utf-8 -*-
"""Module for creating multiple pages"""
"""Insipiration: https://github.com/upraneelnihar/streamlit-multiapps"""
import streamlit as st

def get_position(spages,option):
    for i in range(len(spages)):
        if spages[i]['title'] == option:
            break
    return i

class MultiPage:
    """
    MultiPage class will generate streamlit web app with multiple pages
    """
    def __init__(self, location="body"):
        self.menu = []
        self.location=location

    def add_page(self, title, task):
            self.menu.append({
            "title": title,
            "function": task
        })

    def run(self):
        tot_pages = len(self.menu)
        if self.location =="body":
            cols = st.columns(tot_pages)
        if self.location =="sidebar":
            cols = st.sidebar.columns(tot_pages)
        but_values = [cols[i].button(self.menu[i]['title'],key=self.menu[i]['title']) for i in range(tot_pages)]
        # Query query_params to get the required page
        query_params = st.experimental_get_query_params()
        try:
            query_option = query_params['option'][0]
        except:
            st.experimental_set_query_params(option=self.menu[0]['title'])
            query_params = st.experimental_get_query_params()
            query_option = query_params['option'][0]
        q_index = get_position(self.menu,query_option)

        if "cmenu" not in st.session_state:
            st.session_state.cmenu=0

        if True in but_values:
            c_index = but_values.index(True)
            if q_index is not c_index:
                final = c_index
                st.experimental_set_query_params(option=self.menu[final]['title'])
            else:
                final = q_index
            st.session_state.cmenu=final
        self.menu[st.session_state.cmenu]['function']()
        return self.menu[st.session_state.cmenu]['title']
