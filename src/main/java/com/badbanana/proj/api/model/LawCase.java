package com.badbanana.proj.api.model;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by langley on 15/10/17.
 */
@Entity
public class LawCase {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Setter
    @Getter
    @Column(name = "id")
    public Long id;

    @Setter
    @Getter
    @Column(length = 512)
    public String caseName;

    @Setter
    @Getter
    @Column(length = 512)
    public String jurisdiction;

    @Setter
    @Getter
    public String url;

    @Column(length = 512)
    @Setter
    @Getter
    public String decisionDate;

    @Setter
    @Getter
    public String mnc;

    @Column(length = 20000)
    @Setter
    @Getter
    public String parties;

    @Column(length = 512)
    @Setter
    @Getter
    public String category;

    @Column(length = 20000)
    @Setter
    @Getter
    public String catchwords;

    @Column(length = 20000)
    @Setter
    @Getter
    public String judgment;  // html

    @Column(length = 2000)
    @Setter
    @Getter
    public String decision;

    @Setter
    @Getter
    @OneToMany(cascade = CascadeType.ALL)
    public List<Relevance> relevance = new ArrayList<>();


}
