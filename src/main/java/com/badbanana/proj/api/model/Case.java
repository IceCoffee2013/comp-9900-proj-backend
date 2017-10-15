package com.badbanana.proj.api.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by langley on 15/10/17.
 */
@Entity
public class Case {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Setter @Getter
    public String id;

//    @Setter @Getter
//    @Column(length = 512)
//    public String title;

    @Setter @Getter
    @Column(length = 512)
    public String caseName;

    @Setter @Getter
    @Column(length = 512)
    public String Jurisdiction;

    @Setter @Getter
    public String url;

    @Column(length = 512)
    @Setter @Getter
    public String decisionDate;

//    @Column(length = 512)
//    @Setter @Getter
//    public String lastUpdate;

    @Setter @Getter
    public String mnc;

    @Column(length = 512)
    @Setter @Getter
    public String parties;

    @Column(length = 512)
    @Setter @Getter
    public String category;

    @Column(length = 10000)
    @Setter @Getter
    public String catchwords;

    @Column(length = 20000)
    @Setter @Getter
    public String judgment;  // html

    @Column(length = 2000)
    @Setter @Getter
    public String decision;

    @Setter @Getter
    public List<Relevance> relevance = new ArrayList<>();


}
