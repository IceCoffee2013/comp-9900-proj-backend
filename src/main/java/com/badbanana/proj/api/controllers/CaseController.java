package com.badbanana.proj.api.controllers;

import com.badbanana.proj.api.model.LawCase;
import com.badbanana.proj.api.repository.CaseRepository;
import com.badbanana.proj.api.tool.PythonTools;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

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
    public ResponseEntity<List<LawCase>> getCases(@RequestParam(value = "searchText", required = false) String searchText) {

        List<LawCase> lawCases = new ArrayList<>();
        if (searchText != null && !searchText.isEmpty()) {
            lawCases = this.caseRepository.findByCaseNameContaining(searchText);
        } else {
            lawCases = this.caseRepository.findAll();
        }

        return new ResponseEntity<>(lawCases, HttpStatus.OK);
    }

    @RequestMapping(value = "/detail/{id}", method = RequestMethod.GET)
    public ResponseEntity<LawCase> getCase(@PathVariable Long id) {
        LawCase lawCase = this.caseRepository.findOne(id);
        return new ResponseEntity<>(lawCase, HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.POST)
    public ResponseEntity<?> addCase(@RequestBody LawCase lawCase) {
        LawCase newCase = this.caseRepository.save(lawCase);

        return new ResponseEntity<>(newCase, HttpStatus.CREATED);
    }

    @RequestMapping(value = "/tag/{id}", method = RequestMethod.GET)
    public ResponseEntity<?> getTagFilter(@PathVariable Long id) {
        LawCase lawCase = this.caseRepository.findOne(id);   // TODO
        String result = PythonTools.parse(lawCase.getJudgment());
        return new ResponseEntity<>(result, HttpStatus.OK);
    }


}
