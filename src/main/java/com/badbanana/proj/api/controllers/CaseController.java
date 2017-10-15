package com.badbanana.proj.api.controllers;

import com.badbanana.proj.api.model.LawCase;
import com.badbanana.proj.api.repository.CaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by langley on 15/10/17.
 */
@RestController
@RequestMapping(value = "/api/case")
public class CaseController {

    @Autowired
    private CaseRepository caseRepository;

    @RequestMapping(method = RequestMethod.GET)
    public ResponseEntity<List<LawCase>> getCases() {

        List<LawCase> lawCases = new ArrayList<>();
        lawCases = this.caseRepository.findAll();

        return new ResponseEntity<>(lawCases, HttpStatus.OK);
    }


}
