package com.badbanana.proj.api.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.Setter;
import javax.persistence.*;


/**
 * Created by langley on 15/10/17.
 */

@Entity
public class Relevance {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @JsonIgnore
    @Setter @Getter
    public Long id;

    @Setter @Getter
    public String title;

    @Setter @Getter
    public String url;

    @Setter @Getter
    public String value;

}
