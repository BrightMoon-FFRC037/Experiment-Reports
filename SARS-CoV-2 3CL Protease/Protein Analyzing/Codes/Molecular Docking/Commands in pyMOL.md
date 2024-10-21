```python
select ligand_selection, may16_out  
select receptor_selection, 7en8_clean
select interactions, (ligand_selection within 4 of receptor_selection)
show sticks, interactions

```