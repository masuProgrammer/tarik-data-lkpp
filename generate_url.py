from itertools import product


## URL Data SIRUP
url_data = {
    'prov': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/d5c9a703-07bb-4e87-8e08-ff04b23741b9/json/3325/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/024e7c91-226e-417d-be1a-1667a84595ee/json/3333/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/999bd6d6-9e67-4c7d-83bd-650430ce2fe7/json/3342/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/07f8350f-d005-42ce-bcaf-a39eaf3fbb02/json/3345/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/6d5fd703-2fbe-44fe-8b93-a88ecaaacab3/json/3346/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/865585cb-e72c-41d8-b064-f6dd83253608/json/3348/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/fbfc9ab8-6a71-49d2-a955-7b9e9b57a4fe/json/3349/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/05fe5f87-9547-4a56-991d-041433864211/json/3350/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/ba2c6327-9451-49c9-8c61-408936baaff6/json/4847/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/3adfa365-7962-4994-8bce-4e6ca5e10320/json/6987/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'bky': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/29926865-cf96-40fa-87ef-71497a53c9b8/json/8093/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/27bd3cd4-b772-454a-a11a-f3aa3cfec410/json/8084/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/150a43e4-a51b-4999-a8c5-72a8de03602a/json/8127/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/8c2ef7fa-8c41-452f-a213-92bf8bca8521/json/8091/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/cdc7ff31-a16b-4d03-af9a-0ad532b6706f/json/8104/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/165ca5d0-9c5f-48f2-b238-45d13dea8ac9/json/8129/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/8df010fe-2177-42fa-8533-46ffbd41c146/json/8090/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/2cfd0532-aa67-4103-96ad-be996369339f/json/8094/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/9ea15884-c36b-43cf-a73d-29e6897182ac/json/8106/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/19254004-fca9-4cf3-8717-6c6f179c8671/json/8123/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'mlw': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/bb1daf75-e4c4-453a-bc80-35b6aafc5c25/json/10553/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/06ddfd2e-db4e-4a9f-ac70-c346b21bfcbd/json/10544/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/0d286cd2-a099-404b-a986-c2bdffd8cfd7/json/10587/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/6cbc4e2f-1e08-4206-9377-c890445b93c7/json/10551/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/fe54eaea-2367-4d1c-97d2-8f2f110fb12e/json/10563/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/a84b7d94-2234-487c-b24e-fd93f724a2c0/json/10589/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/4c8cf603-d8dc-47a5-816c-4247269f8232/json/10550/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/775818f0-cfae-4cc7-b794-86ed9b5cdba9/json/10554/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/df38531c-b295-4ddc-84e9-90a0180de60c/json/10565/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/68474130-7fde-46e8-9b37-2ffe58449075/json/10583/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'ptk': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/9660f0a0-2cc2-4c6e-899b-35dad4da6d47/json/3993/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/e417f5ee-d504-4de0-a03d-6084fb521da7/json/4001/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/c6bcddde-9f61-4aeb-814a-667800878a08/json/4010/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/a19f3701-4b9d-4d36-ac86-2f0fd7a08f71/json/4013/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/9786b715-9732-4519-b30a-bf8130a81fa5/json/4014/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/f9ad6a89-56aa-4aea-957a-08c46c3f335c/json/4016/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/aed75afe-a7a1-493c-bce3-021b624dafae/json/4017/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/3d6345b1-9ff4-46f9-bb14-b1e54786b9e2/json/4018/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/3ceb56ea-aa95-4803-94c1-3bb9ed95756e/json/4853/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/8974bad3-4a6c-439f-a408-ea3e28cd5772/json/6993/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'sgu': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/682a965a-5ef0-481b-9729-517a95f5c5fc/json/4116/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/1d52ae98-5104-490e-8333-7e29f211e0d8/json/4124/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/5b67e125-cd9a-4a80-9418-25cf368e4987/json/4133/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/391e5397-b0b4-4959-bda9-71edc926f194/json/4136/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/4abdab3f-d400-46bf-a7d4-246f4059c336/json/4137/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/08a94892-a94f-4370-b1ec-1906ec2dcfd4/json/4139/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/ff54f94b-5c6b-4bb0-b07e-afa2272fd973/json/4140/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/a7af29e3-e7a2-4ee4-9d90-5b409e910d94/json/4141/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/fa9d2a23-cd9a-4dad-a3ab-d6e30aad7e29/json/4850/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/0421b816-6762-42a7-b8f1-840172bd4d06/json/6990/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'skd': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/9ea056a5-2d18-4f9b-a725-05e14e16c5a6/json/11062/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/b44d33a1-5389-4a1b-89cd-766de8565af2/json/11053/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/79cbc43a-07af-4cc0-af1b-32f350e48790/json/11097/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/b1ff7bc7-61ba-4473-99df-5776768c0c32/json/11061/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/46411d73-4af5-450a-8e65-5b7c5da4f5dc/json/11072/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/d3221cef-94e6-4bef-a62d-5b3e22439aeb/json/11098/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/a7548bf7-0f55-4899-a45f-cc623344387a/json/11060/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/c98f286c-50e4-4fbc-8920-c07a50946317/json/11063/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/8a3f94a9-5728-4050-9a0a-adcdd1f2c96b/json/11074/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/91a289a4-be79-46f8-88ab-bd170b6ef035/json/11092/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'kph': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/b70e609f-4c08-4ff3-83c6-2bff13ffc524/json/8962/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/d6738261-cac1-4d8b-abe5-e267eff08e5b/json/8953/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/a3431954-0899-48bc-b6d6-754ede274c28/json/8998/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/285f3d47-f937-405c-bddb-3038ce7d95a1/json/8960/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/57194f10-6c1e-45a4-9a4f-ab667a124168/json/8975/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/37a4dc44-5e80-4be1-9b70-bd6b918689b3/json/9000/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/0b87d709-300d-4733-b196-061ae401075a/json/8959/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/c4432f2b-ea2d-49e9-92b2-e03d13ea65a9/json/8963/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/90e5f253-8d87-4af4-81d6-e890054c9ea1/json/8977/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/ca38d348-3942-4d73-966b-20b029058acf/json/8994/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'kkr': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/902d63e5-1047-4c84-96fe-e83fa4258005/json/4155/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/5e61c88f-da68-440c-81d3-428a2fe6cf44/json/4163/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/0fa6d8cd-c932-45a9-9a88-2fd56ec9fdf4/json/4172/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/77d2c841-d3eb-4c1b-a6ba-be1b08bbad2f/json/4173/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/54946e21-5bf5-4daf-aed9-fcec771d8356/json/4174/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/8fa8616c-03f6-43ae-8b50-e24d5b53ccb6/json/4176/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/42761694-bfac-4ee5-ad34-59ec73568ef8/json/4177/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/d175bb7e-894f-408f-be43-837b0f8533b7/json/4178/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/45a41800-d7b9-4707-ac0a-4815f443f273/json/4855/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/1def2d96-2fc3-455b-a58c-ec15f9236c59/json/6995/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'ldk': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/78fee66a-7941-498e-b58c-097f0cc9a9aa/json/9550/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/e39265fa-b3d9-422e-892f-c77105beb2dd/json/9541/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/65cb52ac-b6b2-49b9-a1c7-e06afeb65a18/json/9584/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/f217a243-6a38-4c87-b8b0-b5e821bd75de/json/9548/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/1edec30f-8378-4be1-a52c-328321e608be/json/9561/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/2b02d689-d435-40bd-972b-461cf1b39de9/json/9586/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/fbef49af-f9f0-45cd-8638-c0ef0f1cff0b/json/9547/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/36ef05a8-0ccb-490d-be31-f3d47c39b0bd/json/9551/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/3d4bafd9-8c53-40cc-b6f1-5d5399af1a86/json/9563/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/43d27e25-ab72-40bf-80b5-34f80e5e99e2/json/9580/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'skw': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/e5898f11-22c3-4311-9314-e8101322b4d1/json/9700/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/9f934500-7b74-4d82-b40c-3440b2f4c6eb/json/9691/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/3d8a90e3-c62c-467b-a874-c97d4467a272/json/9734/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/6bd16793-733b-449d-8665-66c6f0867864/json/9698/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/59b401fe-d1cf-4b2c-80c2-f9745703f53f/json/9711/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/0d009263-4244-4263-b7b7-e020aa4d7ebb/json/9736/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/ac7a6ea4-677f-4b71-b69d-0e1861f4d74a/json/9697/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/87c771c6-744f-4a40-8b49-6a587c2da3d2/json/9701/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/7755339c-82cb-4ed5-b033-f78bf56b04b7/json/9713/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/df277aee-4eac-4e44-957a-783dd3a66f27/json/9730/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'stg': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/c33fae90-52c5-4106-a14e-9715c7e97b36/json/12111/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/8aac33bc-002a-4f92-89bd-f7c18365e3a3/json/12102/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/4c1a9e1f-63fa-4e90-9a92-d4fe263aa5ce/json/12142/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/b7b07bc0-8481-446f-a76b-bf8f8bf45f8e/json/12110/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/9b9cbb5e-9e61-4644-adad-7e22a3246698/json/12120/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/cba8570f-13ab-476a-a781-2916eadb2e0a/json/12143/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/b111f7d3-2f02-49d6-a6cf-16df191a80f7/json/12109/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/9640941b-032b-4858-a91c-259c1e703ec5/json/12112/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/4610f52b-28c6-45ac-b6f9-4cd85a81b671/json/12122/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/b51fc850-69f1-449e-94b8-6aaa295ed9b9/json/12147/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'mpw': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/58dc4d1c-9dca-4587-8d0c-ee2e46e0b6b8/json/12160/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/5cc5ef08-ce37-4b63-b78d-fd56ee323565/json/12151/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/684468d5-3be7-4325-8776-ebea873859d5/json/12191/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/497d58d3-8dee-4555-b5c1-0b1a53115299/json/12159/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/e0fedd5d-288f-466f-bd44-bcd570b911a8/json/12169/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/02cee2d0-1a7c-4a54-9ac3-5afdb4af293f/json/12192/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/ca15f614-a345-4c88-8527-77eb341f2a97/json/12158/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/ee3d9887-927d-4edf-9020-14b20d4d123c/json/12161/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/6a2fa946-fd62-44e6-9d1f-9c3c9b5f9ee4/json/12171/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/dc613579-3241-4371-9c2e-a2f95b893283/json/12196/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'ktp': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/0bd0c5fb-171a-4c12-a2c0-f6fc1759337a/json/11556/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/d8663bfe-d238-4e0d-8324-afbf608dece3/json/11547/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/50405646-142c-4c6b-b580-b2c4902d398f/json/11591/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/eae2d830-4dbc-4f9c-b41e-1b99aa0e912e/json/11555/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/218aad1d-a649-42b4-80f5-bd5a2f139a2e/json/11566/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/15601767-f760-424a-b893-a0695cafa272/json/11592/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/71fab6b4-4358-497d-847a-7d9c6ccc68f8/json/11554/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/b4e6bd3c-7f9b-4fd5-bee7-344c15b1fb05/json/11557/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/17287b83-4ff1-462b-ad63-0193a324089a/json/11568/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/74929947-0837-48f9-99c4-852ebc2fdaf1/json/11586/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    },
    'ktn': {
      'urlRUP_SubKegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/7e64ea83-761a-4046-8d35-6678c7d0b8c7/json/9354/RUP-SubKegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_KegiatanMaster' : "https://isb.lkpp.go.id/isb-2/api/3087d403-bc8c-4deb-beab-8d0da67dacbd/json/9345/RUP-KegiatanMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/31d95dc0-463f-476c-978c-ffebb8ecef4e/json/9388/RUP-PaketPenyedia-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaTerumumkan' : "https://isb.lkpp.go.id/isb-2/api/f800e5a3-2b4b-4b52-af04-4dd20953fda8/json/9352/RUP-PaketSwakelola-Terumumkan/tipe/4:12/parameter/",
      'urlRUP_ProgramMaster' : "https://isb.lkpp.go.id/isb-2/api/bcb54580-0ec4-442e-b581-c0f27ea59c31/json/9365/RUP-ProgramMaster/tipe/4:12/parameter/",
      'urlRUP_PaketPenyediaLokasi' : "https://isb.lkpp.go.id/isb-2/api/8fa244e8-d980-46c9-8dd7-0dff2716871b/json/9390/RUP-PaketPenyediaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketSwakelolaLokasi' : "https://isb.lkpp.go.id/isb-2/api/51fc473f-3cad-4030-a649-be0948f8c38e/json/9351/RUP-PaketSwakelolaLokasi/tipe/4:12/parameter/",
      'urlRUP_PaketAnggaranPenyedia' : "https://isb.lkpp.go.id/isb-2/api/cef78066-448e-481a-a252-ff8a5cd814d5/json/9355/RUP-PaketAnggaranPenyedia/tipe/4:12/parameter/",
      'urlRUP_MasterSatker' : "https://isb.lkpp.go.id/isb-2/api/41dde050-e0b3-478f-b13a-0d5907002ca2/json/9367/RUP-MasterSatker/tipe/12:12/parameter/",
      'urlRUP_StrukturAnggaran' : "https://isb.lkpp.go.id/isb-2/api/8004f7b5-208e-4501-9e35-c40ad790aac3/json/9384/RUP-StrukturAnggaranPD/tipe/4:12/parameter/"
    }
}


# Fungsi Read JSON dan Konversi ke Excel
def generateURL(jenisdata, kode, tahun):
    ## Kode berdasarkan lokasi UKPBJ
    kodeRUP = None  # Initialize with a default value
    kodeLPSE = None  # Initialize with a default value
    ## Kode berdasarkan lokasi UKPBJ
    if kode == "prov":
        kodeRUP = "D197"
        kodeLPSE = "97"
    if kode == "bky":
        kodeRUP = "D206"
        kodeLPSE = "444"
    if kode == "mlw":
        kodeRUP = "D210"
        kodeLPSE = "540"
    if kode == "ptk":
        kodeRUP = "D199"
        kodeLPSE = "62"
    if kode == "sgu":
        kodeRUP = "D204"
        kodeLPSE = "298"
    if kode == "skd":
        kodeRUP = "D198"
        kodeLPSE = "175"
    if kode == "kph":
        kodeRUP = "D209"
        kodeLPSE = "488"
    if kode == "kkr":
        kodeRUP = "D202"
        kodeLPSE = "188"
    if kode == "ldk":
        kodeRUP = "D205"
        kodeLPSE = "496"
    if kode == "skw":
        kodeRUP = "D200"
        kodeLPSE = "132"
    if kode == "stg":
        kodeRUP = "D211"
        kodeLPSE = "345"
    if kode == "mpw":
        kodeRUP = "D552"
        kodeLPSE = "118"
    if kode == "ktn":
        kodeRUP = "D236"
        kodeLPSE = "438"

    ## Membuat parameter service data LKPP
    if jenisdata == "RUPSubKegiatanMaster":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_SubKegiatanMaster']}{kodeJSON}"
    if jenisdata == "RUPKegiatanMaster":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_KegiatanMaster']}{kodeJSON}"
    if jenisdata == "RUPPaketPenyediaTerumumkan":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_PaketPenyediaTerumumkan']}{kodeJSON}"
    if jenisdata == "RUPPaketSwakelolaTerumumkan":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_PaketSwakelolaTerumumkan']}{kodeJSON}"
    if jenisdata == "RUPProgramMaster":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_ProgramMaster']}{kodeJSON}"
    if jenisdata == "RUPPaketPenyediaLokasi":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_PaketPenyediaLokasi']}{kodeJSON}"
    if jenisdata == "RUPPaketSwakelolaLokasi":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_PaketSwakelolaLokasi']}{kodeJSON}"
    if jenisdata == "RUPPaketAnggaranPenyedia":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_PaketAnggaranPenyedia']}{kodeJSON}"
    if jenisdata == "RUPMasterSatker":
        kodeJSON = f"{kodeRUP}:{tahun}"
        urlFile = f"{url_data[kode]['urlRUP_MasterSatker']}{kodeJSON}"
    if jenisdata == "RUPStrukturAnggaran":
        kodeJSON = f"{tahun}:{kodeRUP}"
        urlFile = f"{url_data[kode]['urlRUP_StrukturAnggaran']}{kodeJSON}"

    return urlFile

kodes = ["PROV", "BKY", "MLW", "PTK", "SGU", "SKD", "KPH", "KKR", "LDK", "SKW", "STG", "MPW", "KTN"]

kodes = [kode.lower() for kode in kodes]
jenisdatas = ["RUPSubKegiatanMaster", "RUPKegiatanMaster", "RUPPaketPenyediaTerumumkan", "RUPPaketSwakelolaTerumumkan", "RUPProgramMaster", "RUPPaketPenyediaLokasi",
              "RUPPaketSwakelolaLokasi", "RUPPaketAnggaranPenyedia", "RUPMasterSatker", "RUPStrukturAnggaran"]
tahuns = ["2022", "2023","2024"]

# Generate and save URLs to a text file
with open("generated_urls.txt", "w") as file:
    for combination in product(jenisdatas, kodes, tahuns):
        url = generateURL(*combination)
        file.write(url + "\n")

print("URLs generated and saved to generated_urls.txt")








