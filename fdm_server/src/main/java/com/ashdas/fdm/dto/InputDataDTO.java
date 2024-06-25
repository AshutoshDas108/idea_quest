package com.ashdas.fdm.dto;

import lombok.*;
import org.springframework.format.annotation.DateTimeFormat;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class InputDataDTO {

    private Float amount;
    private String merchant;
    private Integer age;
    private String city;
    private String state;
    private  Float lat;
    private  Float longi;
    private Integer hour;

}
