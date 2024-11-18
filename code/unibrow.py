'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "csv", "json"])

if uploaded_file is not None:
    try:
        file = uploaded_file.name
        df = pl.load_file(uploaded_file, pl.get_file_extension(file))

        if df is not None:
            st.subheader("Data Filtering")

            all_columns = pl.get_column_names(df)
            columns = st.multiselect(
                "Select columns to display", all_columns, default=all_columns
            )

            if columns:
                filtered_df = df[columns]

                text_columns = pl.get_columns_of_type(filtered_df, "object")
                if text_columns:
                    text_column = st.selectbox(
                        "Select a text column to filter (optional)",
                        ["None"] + text_columns,
                    )
                    if text_column != "None":
                        unique_values = pl.get_unique_values(filtered_df, text_column)
                        text_values = st.multiselect(
                            "Select values to filter", unique_values
                        )

                        if text_values:
                            filtered_df = filtered_df[
                                filtered_df[text_column].isin(text_values)
                            ]

                        # Display Filtered Data
                        st.subheader("Filtered Data")
                    else:
                        st.subheader("Data")

                st.write(filtered_df)

                # Row count information
                st.info(f"Showing {len(filtered_df)} rows out of {len(df)} total rows")

                # Statistics Section using pandaslib
                st.subheader("Numerical Statistics")
                float_columns = pl.get_columns_of_type(filtered_df, "float64")
                int_columns = pl.get_columns_of_type(filtered_df, "int64")
                numeric_columns = float_columns + int_columns

                if numeric_columns:
                    numeric_df = filtered_df[numeric_columns]
                    st.write(numeric_df.describe())
                else:
                    st.write("No numerical columns selected for statistics")

            else:
                st.warning("Please select at least one column to display")

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
else:
    st.write("No file uploaded")
    st.stop()
