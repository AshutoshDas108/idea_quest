package com.ashdas.fdm.controller;

import com.ashdas.fdm.dto.InputDataDTO;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class MLController {

    // Update the URL to use the Docker service name for Flask app
    private static final String FLASK_APP_URL = "http://flask_app:5000/api/predict";


    @PostMapping("/predict")
    public String predict(@RequestBody InputDataDTO data){

        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<InputDataDTO> entity = new HttpEntity<>(data, headers);

        try {
            ResponseEntity<String> response = restTemplate.exchange(
                    FLASK_APP_URL,
                    HttpMethod.POST,
                    entity,
                    String.class
            );

            return response.getBody();
        } catch (Exception e) {
            // Handle exceptions or return appropriate error response
            e.printStackTrace();
            return "Error communicating with Flask app: " + e.getMessage();
        }
    }
}
