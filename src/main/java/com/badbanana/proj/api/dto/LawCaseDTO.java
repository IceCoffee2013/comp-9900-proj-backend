package com.badbanana.proj.api.dto;

import com.badbanana.proj.api.model.Relevance;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by langley on 15/10/17.
 */
public class LawCaseDTO {

    @Setter
    @Getter
    public Long id;

    @Setter
    @Getter
    public String caseName;

    @Setter
    @Getter
    public String Jurisdiction;

    @Setter
    @Getter
    public String url;

    @Setter
    @Getter
    public String decisionDate;

    @Setter
    @Getter
    public String mnc;

    @Setter
    @Getter
    public String parties;

    @Setter
    @Getter
    public String category;

    @Setter
    @Getter
    public String catchwords;

    @Setter
    @Getter
    public String judgment;  // html

    @Setter
    @Getter
    public String decision;

    @Setter
    @Getter
    public List<Relevance> relevance = new ArrayList<>();

    @Setter
    @Getter
    public QueryDTO queryDTO;

}
