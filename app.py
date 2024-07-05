# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Credit Card Eligible </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_creditcard.pkl', 'rb'))


# Opsi pilihan

gender_options = {
    'Female': 0,
    'Male': 1
}

display_gender_options = {v: k for k, v in gender_options.items()}

general_options = {
    'Tidak' : 0,
    'Ya' : 1
}

display_general_options = {v: k for k, v in general_options.items()}

# Pilihan utama

pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi dari file csv','Input Manual'])

if pilihan == 'Prediksi dari file csv':
    # Mengupload file
    upload_file = st.file_uploader('Pilih file csv', type='csv')
    if upload_file is not None:
        dataku = pd.read_csv(upload_file)
        st.write(dataku)
        st.success('File berhasil diupload')
        hasil = my_model.predict(dataku)
        #st.write('Prediksi',hasil)
        # Keputusan
        hasil_df = pd.DataFrame(hasil, columns=['Hasil Predict'])

        # Add an ID column if it's not already in the uploaded file
        if 'ID' not in dataku.columns:
            dataku['ID'] = range(1, len(dataku) + 1)

        # Create a DataFrame with only ID and prediction results
        hasil_akhir = dataku[['ID']].copy()
        hasil_akhir['Hasil Predict'] = hasil
        
        # Add a text input for searching merchant name
        id_search = st.text_input('Search ID')
                
        if id_search:
            id_search = int(id_search)  
            # Filter transactions for the given merchant name
            id_df = hasil_akhir[hasil_akhir['ID'] == id_search]

            if not id_df.empty:
                id_df['target Status'] = id_df['Hasil Predict'].apply(lambda x: 'Elligible' if x == 1 else 'Not Elligible')
                st.write(f"Status untuk id '{id_search}':")
                st.dataframe(id_df[['ID', 'Hasil Predict', 'target Status']], width=400, height=300)
            else:
                st.warning(f"Tidak ada id '{id_search}'")

        # Display the DataFrame with the predictions
        st.write("**Data Hasil Prediksi**")
        st.dataframe(hasil_akhir, width=400, height=300)
    else:
        st.error('File yang diupload kosong, silakan pilih file yang valid')
        #st.markdown('File yang diupload kosong, silakan pilih file yang valid')
else:
   # Baris Pertama
   with st.container():
       col1,  = st.columns(1)
       with col1:
           id = st.number_input('ID', value=000000)
           
   # Baris Kedua
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
        # Show the selectbox with descriptive labels
        selected_gender_label = st.selectbox('Gender', options=list(gender_options.keys()))
        
        # Get the corresponding value for the selected label
        gender = gender_options[selected_gender_label]
        
       with col2:
           # Show the selectbox with descriptive labels
        selected_mobil_label = st.selectbox('Memiliki mobil', options=list(general_options.keys()))
        
        # Get the corresponding value for the selected label
        car = general_options[selected_mobil_label]

        with col3:
            # Show the selectbox with descriptive labels
            selected_property_label = st.selectbox('Memiliki property', options=list(general_options.keys()))

            # Get the corresponding value for the selected label
            property = general_options[selected_property_label]

   # Baris Ketiga
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
        # Show the selectbox with descriptive labels
        selected_workPhone_label = st.selectbox('Memiliki Telepon Kantor', options=list(general_options.keys()))
        
        # Get the corresponding value for the selected label
        workPhone = general_options[selected_workPhone_label]
        
       with col2:
           # Show the selectbox with descriptive labels
        selected_telepon_label = st.selectbox('Memiliki telepon', options=list(general_options.keys()))
        
        # Get the corresponding value for the selected label
        phone = general_options[selected_telepon_label]

        with col3:
            # Show the selectbox with descriptive labels
            selected_email_label = st.selectbox('Memiliki email', options=list(general_options.keys()))

            # Get the corresponding value for the selected label
            email = general_options[selected_email_label]
            
   # Baris Keempat
   with st.container():
       col1, col2, col3, col4 = st.columns(4)
       with col1:
        # Show the selectbox with descriptive labels
        selected_pengangguran_label = st.selectbox('Apakah Pengangguran', options=list(general_options.keys()))
        
        # Get the corresponding value for the selected label
        pengangguran = general_options[selected_pengangguran_label]
        
       with col2:
        num_children = st.number_input('Jumlah Anak', value=0)

       with col3:
        num_family = st.number_input('Jumlah Keluarga', value=0)
        
       with col4:
        acc_length = st.number_input('Panjang Akun', value=0)
       
   # Baris Kelima
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
            income = st.number_input('Gaji', value=0)
       with col2:
            age = st.number_input('Umur', value=0) 
       with col3:
            year_employ = st.number_input('Lama Kerja', value=0)

   # Baris Keenam
   with st.container():
       col1, col2 = st.columns(2)
       with col1:
           inc_type = st.selectbox('Tipe Gaji',['Commercial associate','Pensioner', 'State servant', 'Student', 'Working'])
       with col2:
           edu_type = st.selectbox('Tipe Edukasi',['Academic degree','Higher education', 'Incomplete higher', 'Lower secondary', 'Secondary / secondary special'])

   # Baris Ketujuh
   with st.container():
       col1, col2, col3 = st.columns(3)
       with col1:
           family_status = st.selectbox('Status Keluarga',['Civil marriage','Married', 'Separated', 'Single / not married', 'Widow'])
       with col2:
           house_type = st.selectbox('Tipe Rumah',['Co-op apartment','House / apartment', 'Municipal apartment', 'Office apartment', 'Rented apartment', 'With parents'])
       with col3:
           occ_type = st.selectbox('Occupation Type', [
                                    'Security Staff', 'Sales Staff', 'Accountants', 'Laborers',
                                    'Managers', 'Drivers', 'Core Staff', 'High Skill Tech Staff',
                                    'Cleaning Staff', 'Private Service Staff', 'Low-Skill Laborers',
                                    'Cooking Staff', 'Medicine Staff', 'Secretaries',
                                    'Waiters/Barmen Staff', 'HR Staff', 'Realty Agents', 'IT Staff'
                                ])    


   # Inference
   data = {
           'ID': id,
           'Gender': gender,
           'Own_car': car,
           'Own_property': property,
           'Work_phone': workPhone,
           'Phone': phone,
           'Email': email, 
           'Unemployed': pengangguran,
           'Num_children': num_children,
           'Num_family': num_family,
           'Account_length': acc_length,
           'Total_income': income,
           'Age': age,
           'Years_employed': year_employ,
           'Income_type': inc_type,
           'Education_type': edu_type,
           'Family_status': family_status,
           'Housing_type': house_type,
           'Occupation_type': occ_type
           }

   # Tabel data
   kolom = list(data.keys())
   df = pd.DataFrame([data.values()], columns=kolom)
   
   # Melakukan prediksi
   hasil = my_model.predict(df)
   hasil_proba = my_model.predict_proba(df)
   keputusan1 = round(float(hasil_proba[:,0])*100,2)
   keputusan2 = round(float(hasil_proba[:,1])*100,2)


   # Memunculkan hasil di Web 
   st.write('***'*10)
   st.write('<center><b><i><u><h3>ID', str(id),'</b></i></u></h3>', unsafe_allow_html=True)
   st.write('<center><b><h4>Probabilitas Layak = ', str(keputusan1),'%</b></h4>', unsafe_allow_html=True)
   st.write('<center><b><h4>Probabilitas Tidak Layak = ', str(keputusan2),'%</b></h4>', unsafe_allow_html=True)