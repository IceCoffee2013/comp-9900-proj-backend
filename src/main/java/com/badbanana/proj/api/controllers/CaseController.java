package com.badbanana.proj.api.controllers;

import com.badbanana.proj.api.repository.CaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

/**
 * Created by langley on 15/10/17.
 */
@Controller
public class CaseController {

    @Autowired
    private CaseRepository caseRepository;

    public CaseController() {
    }



}
