## Files for Power Ranch

Files for the Power Ranch model used in this paper:
Sen, S., Roesler, J., Ruddell, B., & Middel, A. (2019). Cool Pavement Strategies for Urban Heat Island Mitigation in Suburban Phoenix, Arizona. *Sustainability*, 11(16), 4452.

Run on OpenFOAM v 6.0 and Python3

### To use 
Navigate to any of the folders.

Generate the mesh

```
gmsh -3 PowerRanchArea.geo PowerRanchArea.msh
```

Import the mesh into OpenFOAM:

```
gmshToFoam PowerRanchArea.msh
```
Modify polyMesh with this command (based on `changeDictionaryDict`):

```
changeDictionary
```

Run the following command from the terminal inside any of the folders:

```bash
bash runthis
```

The following processes will be run:

1. Any leftover processor or post-processing folders will be deleted
2. Any leftover log files will be deleted (use `mv` to rename if you need it!)
3. Any intermediate output folders will be deleted
4. The domain will be decomposed based on `decomposeParDict`
5. Parallel run of renumberMesh (edit to specify number of processors; use `nproc`to check how many are available)
6. The solver is run (buoyantBoussinesqSimpleFoam; OpenFOAM v 7.0 uses a different command)
7. Subdomain solutions are reconstructed 
8. Post-processing steps executed (varies, check individual files)
9. Shutdown instance (**IMPORTANT:** Comment this out if you don't need it!)

Use the following command to plot residuals and other plots:

```bash
bash plotthis
```
