package com.dec27InfoSolutions.kwizo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.AutoCompleteTextView;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    AutoCompleteTextView user_email , user_pass;
    Button  Login_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViews();


    }

    private void findViews() {
        user_email = findViewById(R.id.atvEmailLog);
        user_pass = findViewById(R.id.atvPasswordLog);
        Login_btn = findViewById(R.id.btnSignIn);
    }
}
