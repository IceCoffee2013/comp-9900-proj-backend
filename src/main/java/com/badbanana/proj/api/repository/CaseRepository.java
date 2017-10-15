package com.badbanana.proj.api.repository;


import com.badbanana.proj.api.model.LawCase;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * Created by langley on 8/5/17.
 */
public interface CaseRepository extends JpaRepository<LawCase, Long> {

}
