from itertools import product


## URL Data SIRUP
url_data = {
  'prov': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/8898bed0-3d2a-4ce7-ae26-2d87f6792447/json/3334/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/d1b11a11-29cc-4665-962e-8aea10c00e33/json/3337/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/3c675a2d-0ef8-4190-9471-4471783d5d83/json/3338/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/2a7b43bc-e129-4432-98c0-870a8bb61096/json/3339/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/dc58375a-199b-4696-b1a1-f17e36e580e8/json/3347/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/f2f596dc-b82e-4eab-86f2-67f802a1a76c/json/3353/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/ea865d3e-3e94-4f29-8e54-5b45e4a5d3d7/json/3354/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/db1bb5c0-d80c-4d47-a478-e17fccb0e302/json/3355/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/d4538ef1-6212-4e2d-8e1f-f60591a593ff/json/3356/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/b4c3f8c6-d82c-437a-b6b4-59907c447b1b/json/3813/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/886f814c-4cca-4bf6-bd91-66c448123600/json/3878/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/1812800c-bfed-437d-bee9-26ed8b0fd955/json/3951/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/a9e5b43f-20f6-45df-84a9-8909ad4ad719/json/5493/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/df4f428b-1044-44ba-8e7e-21ce86ad52b9/json/5843/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/585d9bbb-831a-48e1-b705-1c3b7437315d/json/5943/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/0517feff-8aec-4834-8610-1ea2f170c1f2/json/6043/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/74de6a0d-446c-463a-bf57-bc3713d5a1da/json/6552/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/4172a748-bddc-448b-8b82-77b211257665/json/6660/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/3a4b4b3c-0f26-4f19-8e19-5c07cf145ef6/json/6768/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/a93fa824-9c8e-480d-9deb-ff69f4bcd8bf/json/6876/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'bky': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/0eef3385-ae3e-4ee8-9cb0-164bbd01b2c2/json/8109/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/287d6e33-5871-4dcc-8edf-faf1cff5bf53/json/8108/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/12f4cbac-b25f-4eee-938c-43c391dfa6fb/json/8101/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/4bf3e97e-82e8-4c62-b34d-a5bb54b68639/json/8107/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/c9c2e644-62f1-49d3-9f75-b5a58d4651e6/json/8100/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/fb27633f-e237-42c9-8863-4889d0008f3c/json/8118/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/e6d36aa3-c59a-4257-be3f-f83d28d1082e/json/8120/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/287c76af-1ee1-4368-9fca-6cec8dcb368e/json/8116/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/cb3ce43e-f2d6-4b67-8fce-7ef8bb3abd47/json/8117/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/70070ea9-1dc5-4285-b1b9-a0cc4f214732/json/8124/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/a1117182-6502-4721-ad2d-4abd9d7b74a2/json/8126/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/92ca0ef7-122f-4b67-8b6a-24af56502286/json/8130/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/4a8f68ed-a59e-43f5-ad3d-2c046d3e2c7a/json/8114/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/8abdbfef-936e-48f6-b08c-b6350019ee88/json/8111/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/df57433e-fd79-41dc-9c4e-985f345aeb5c/json/8113/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/780b2664-11d4-4fa6-8faf-f3962aa5f195/json/8112/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/0115a18c-4169-4931-9a58-e6f07158add8/json/8092/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/5ff9c609-6dd6-42bd-8c02-54f3d92899a5/json/8125/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/3c680a9f-cc7e-4282-918c-bff1a87d9cd6/json/8103/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/f9a2fbd8-9bec-41c4-b180-ed701a10d307/json/8102/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'mlw': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/b870c016-437d-43ef-aefb-041bcb9d3146/json/10568/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/febd46bf-8f63-4c87-9a3f-90ced4f179f3/json/10567/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/b014dc41-d6a5-49b4-a556-5885db09555c/json/10591/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/29b3fc8c-2928-4fde-84c3-09efdb7fd839/json/10566/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/1ff7f430-112c-463c-a47c-f40c9383b025/json/10592/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/ee706e78-779a-44ee-a10f-1d9dee24799b/json/10578/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/8ebfde5f-b699-4858-9dc3-4e76bb41ffec/json/10580/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/9065ffdf-0d3d-4070-9732-bb7eb883f0e1/json/10576/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/ec1fea33-6267-4db5-82ea-5514580bba00/json/10577/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/14998c78-476b-46a6-8776-9062c47cf838/json/10584/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/87a745b6-b3d6-465b-b15f-b7c064790b15/json/10586/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/ef7bbb3d-f9f8-48cf-8c28-44e21b1afff7/json/10590/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/6a3ec904-abba-4c40-83af-72fe84a38d88/json/10573/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/0f848d35-a8d0-48d8-8700-47b30a7f93c7/json/10570/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/29fc4019-3f5b-4b37-be1a-9514dbdab7b5/json/10572/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/1a508485-aaba-4081-83a6-1cff73b9cb8c/json/10571/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/a3ced513-1030-46bb-a319-6853c317090c/json/10552/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/ced68093-f887-4332-83a9-931046c2a448/json/10585/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/f21fd440-fa9e-48aa-917f-3db705b479b3/json/10562/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/f3370f2b-24e1-4144-9eeb-1b5a172ae7bb/json/10561/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'ptk': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/44f76f88-57e5-404f-ad66-fe4e793daeef/json/4002/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/5ae7b684-d3fd-4141-87bf-b8ae77fa86c6/json/4005/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/08f3b26b-86e5-4392-bd80-f33055f88d3c/json/4006/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/fb5e1743-5886-41b1-a92b-8afd1c4db084/json/4007/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/56f38683-b58e-45fa-8397-4251c9bee54b/json/4015/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/afbea441-adf3-4ccc-8c39-4fb781fd474c/json/4021/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/6a1e802d-3062-4200-826b-cc8dccadb038/json/4022/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/d907325c-9d11-4ef5-8f82-b1ad25659323/json/4023/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/42adbe89-3f7a-4488-8f7b-fdf6a535956a/json/4024/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/434c7e60-01b8-4548-a031-0940cccd7770/json/4029/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/bbe27c41-c262-4698-8626-635e32a3edd2/json/4030/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/389757d4-e10b-4679-8c91-861dd66a9c27/json/4031/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/622501aa-1463-4a63-8e80-b5e6b26292d9/json/5499/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/760ed651-aa8d-4aa2-b4b5-ec083ea68416/json/5849/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/245dd9a3-466a-4c1e-9ddc-09cdd6fc8dc6/json/5949/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/9d956984-3a81-4d48-868c-8744a6065a0d/json/6049/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/bed45f05-53e3-4230-b743-e4860f4d456a/json/6558/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/affab3ce-eb04-4410-a329-3af7266ef323/json/6666/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/2260659d-2f1a-4ad4-b646-b7d7f813c582/json/6774/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/b2d303ee-401a-4567-850a-4773c15e9325/json/6882/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'sgu': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/34119be6-7b4a-434f-8b0e-659abfc39f62/json/4125/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/896d3adf-e4b9-418e-adfa-b675c644c6ca/json/4128/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/08851528-bbe9-4a8b-b300-188ae514a5f4/json/4129/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/dcf65e8f-1f84-4911-8e20-521e3e937b2e/json/4130/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/7aebee83-63ef-4adf-8f97-807129f2c389/json/4138/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/175d5a9a-f095-46c1-b19c-95f97676be2e/json/4144/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/f7ff6584-4e71-4c90-ba77-4b2d8e53b53f/json/4145/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/e58161cc-89a0-4e32-87f1-26b4e260da2a/json/4146/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/5e124608-09d9-4834-a3b4-266fbbd8483f/json/4147/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/f6db5731-b487-4449-b5bb-67a67018120e/json/4152/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/02e58806-698c-4b26-bf26-0413c75315ed/json/4153/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/7bb953c0-3f55-49a6-a0e6-e56b68592405/json/4154/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/e4bff688-9717-48dc-95e9-7c752eb534ee/json/5496/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/aa601435-518d-491c-9733-f8f64cf2a059/json/5846/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/bb3227c3-843e-4183-a0db-2e88e56583ec/json/5946/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/8121a355-078e-4d19-afea-379b610fea3e/json/6046/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/950897c6-eaa3-4a1f-ab15-bed708d1f4a2/json/6555/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/1352a8e2-408f-43e8-94b5-21c673ba38e6/json/6663/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/93f39f14-4ada-4d16-bc51-da2de49ba9eb/json/6771/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/09a56502-d675-4638-be2f-73d914f79e35/json/6879/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'skd': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/ff154baf-f101-4117-9321-366ec96fc943/json/11077/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/41708671-cb9b-40d6-ab4e-05a9560b141e/json/11076/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/8ef1eb62-2a29-4191-b750-16b2654f07e5/json/11100/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/1842aa60-9068-4380-9c54-aa49de1ed018/json/11075/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/7360103f-fdcb-40a7-b4a5-44327a91c4d4/json/11101/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/eb3343eb-0911-47e9-bc2a-e3bbc87a9e0f/json/11087/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/d42266a6-ce7e-4b47-8fb3-882487fa42bc/json/11089/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/5439ed5e-b77a-4407-a70a-57d6d9d7da7c/json/11085/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/20eef5c4-603b-4114-afe2-65ffb73ac34c/json/11086/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/d6d02a41-ba48-4641-92e9-d855c6bbdaab/json/11093/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/8c0347b3-9b1b-4d17-ac7a-c0284c12b0ef/json/11096/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/df4e6fe4-82c1-46fb-83ee-e786cf688ed2/json/11099/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/f6dd8252-6be5-4ce6-a194-bba2354cb98e/json/11082/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/921fb2da-3645-4337-9783-43b618b606ae/json/11079/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/e176a21e-2962-4349-9169-fb3544d89c24/json/11081/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/01e42711-ae58-4622-b9ca-e8cb75fd66a0/json/11080/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/791049cd-9128-4717-be41-cff45bbbe5fe/json/11057/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/75327743-b92e-4f2c-af01-347722be7ac6/json/11095/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/75f6ce73-e657-4e34-b740-fcee61d02717/json/11071/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/5f067b94-0300-4ddc-9300-788299281693/json/11070/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'kph': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/524a1346-8426-4871-a7bc-0fbb2c13092f/json/8980/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/cc34724a-d376-4b57-b1f6-f9b7c01c93c5/json/8979/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/7295677f-4155-4670-9235-3503321962bc/json/8972/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/f7b68323-5ed5-4091-87c2-7a6ee0032fa1/json/8978/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/74475b91-79fd-41dc-b165-61bdc1a7c761/json/8971/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/dd9ca110-7fd2-4a05-9f3f-e0e0030d6406/json/8989/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/d5ef9fb0-2717-494d-aab6-906443d3e798/json/8991/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/21066a59-f40e-440d-9b56-97514e49d531/json/8987/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/6e2b29b3-cb51-4a38-b2e2-2886bda212c7/json/8988/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/1e2335b6-60b8-4b97-a8db-d3fcc8407b6e/json/8995/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/1b4f3d2b-d066-4598-98c6-70975280784b/json/8997/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/cb345bcb-4240-46b7-bcb9-b699f511b621/json/9001/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/fdd8e4c0-db4a-48e7-a4b5-9990cfb05106/json/8985/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/7626b67a-792d-4c75-bd7c-34e362e93556/json/8982/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/3e5079d9-fb46-405d-b652-95213deec675/json/8984/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/da1add29-a1ba-4412-8341-886f4199f560/json/8983/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/6079f746-85f8-4e44-bf5f-5ca68a3861e3/json/8961/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/4bb14902-cf10-4117-8b10-b7c631e742b8/json/8996/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/1db3460e-2642-40a0-942b-5604f2f5dc75/json/8974/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/7c624cab-f2e9-44c1-aef2-89563be9f5d8/json/8973/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'kkr': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/bc52395d-672c-4831-8ecf-e7dd3cae31fd/json/4162/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/0754f5f3-8416-4c84-9669-263080ce1029/json/4167/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/a35b85a6-ac60-46e3-a30d-a1ae76f7062a/json/4168/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/88c1976b-c6de-449a-9ebc-8f19cd7a58aa/json/4169/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/fd8a8f59-7ca4-4049-9ca4-962eec955cde/json/4175/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/582afcf8-02b9-4620-b377-1a62b9100e71/json/4181/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/074c8396-811c-4e17-8a33-c81927f56bd1/json/4182/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/5baac354-9687-44b4-9646-702cbfa6c961/json/4183/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/a69f4550-e0c6-43a2-b87a-6d767665736f/json/4184/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/0c314efd-0a50-42ca-8316-e7f6d5e3d999/json/4189/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/e67b9b1c-7c90-46e2-a4e5-513cc10ad5d7/json/4190/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/8ac8edd1-9887-4f60-bff0-d8a31397fdbf/json/4193/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/58f0de3f-c5c9-4022-a1ca-72d76df562e2/json/5501/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/8a6570dc-37dd-4d34-92e0-adadabde7e0a/json/5851/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/1345f512-f9a4-460b-acd6-77e8aae6db8c/json/5951/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/9008c962-e4cb-4c7d-a480-4d5428a6cfb1/json/6051/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/8b2d0975-be79-4f67-b33a-54478c9f1e96/json/6560/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/b748476e-9212-4f86-af62-e5248647d82f/json/6668/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/5e7fc98c-88dc-4945-940c-3fd0a51daebe/json/6776/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/b3c73bf8-e60a-4f6f-bca2-5e389cb2a60d/json/6884/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'ldk': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/0627db4d-441b-4f02-a619-aa2080464176/json/9566/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/70d3c172-865c-4bb1-bf42-e04d071a6397/json/9565/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/20b3827d-4480-4599-ae14-56938b37cfb4/json/9588/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/1af3c218-7ffe-426a-b5d5-965646f38c70/json/9564/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/07c6eaf4-b9eb-4775-9295-7febd707fa79/json/9589/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/323c0ad5-9143-49d4-a98d-85e59df1375c/json/9575/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/088b6626-b417-4c8a-a6d5-2d8ed210847e/json/9577/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/0b427a42-cc00-4670-aa77-fd31fd054775/json/9573/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/7a2c9c1a-ce48-4a11-978e-2e4b849c116b/json/9574/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/288e222c-b217-4122-bf76-8108538de2a3/json/9581/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/b426d9b4-35b3-47ff-8f66-1536b982aa8f/json/9583/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/38705ed9-0942-417f-ab6c-7336c8f36402/json/9587/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/0960cee8-9c6f-4ee2-aa78-fea9284aa0f1/json/9571/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/db797021-3d42-4047-9b4e-cbc8acd1399f/json/9568/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/60ae4db4-8f83-4bd5-be68-ac55fc607561/json/9570/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/d8bf3f2c-3614-41e1-b6ac-687af59af33e/json/9569/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/ded9e876-9003-40f2-b73c-22496455a136/json/9549/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/589d9d1f-7f6b-47ed-ae27-31f172ed05f8/json/9582/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/251fed79-1cd2-44ab-af6e-f573e175835c/json/9560/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/cb1f1f15-6941-484c-ad37-7e69c3b76c0e/json/9559/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'skw': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/18fcb7d9-1cb4-4c47-8699-46f579748cc1/json/9716/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/5b15aa33-f696-43ef-aa01-08594fcdde5f/json/9715/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/3ef56f3c-1d30-4988-8ad1-7825b9aaa804/json/9738/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/9b6aab5e-230d-40b3-b30d-d11da980e92b/json/9714/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/68537df6-2e4f-4043-82cc-dbdd0b662069/json/9739/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/e465badb-3ce7-488d-803a-b4d78730715b/json/9725/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/97c0d83d-ec30-4609-8a16-21ef0cc3d35b/json/9727/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/3b5b05fa-6904-4b6b-8d84-72ce16c60ee2/json/9723/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/42f917e3-3781-49a1-a17d-1b4d71bb6488/json/9724/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/bb39f701-83ed-47c7-a051-35479a374ff8/json/9731/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/c6e52332-aeb8-47df-be17-89ac90d8ff5f/json/9733/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/093da2fd-6030-4394-b34d-9ff59e764b3c/json/9737/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/a61718bf-3f0b-4a11-a591-175888bcdfed/json/9721/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/b545dc6f-5b2e-407e-a2b4-16b2fd1444c4/json/9718/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/190403a1-d6b9-44e5-adc9-4fa78408e4c9/json/9720/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/576a6615-fd56-411b-98c2-03c31833d6a8/json/9719/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/6ab5e5aa-f6dd-405c-a080-77fc11689a23/json/9699/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/b04eee87-d45f-45f2-b67e-43f0a68256af/json/9732/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/cc43a11f-b94e-4635-acfd-5d5134fde952/json/9710/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/007a73ca-a71e-44a1-9a1d-a52d711d7b4e/json/9709/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'stg': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/9d4b4400-d290-4300-8481-44ca709e278a/json/12125/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/2be89c0a-58a2-4a85-ba55-59bcb0438a38/json/12124/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/f2aeefc2-179b-43ce-a3e2-6cd104a4e41d/json/12145/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/7a6e1139-95b2-4b8e-bd1d-aa163f0bf6f6/json/12123/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/56acf923-60e4-4dc2-9545-6ade1be8ed6c/json/12146/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/924a1b76-fb13-4fdb-bdb6-ff1ccfadfdce/json/12134/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/bad6b302-30c4-4bca-8c09-4caa6ccb0b5f/json/12135/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/01370e11-e332-4dfc-ac5a-113ed70a33e0/json/12132/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/46a5696d-7f01-4654-a72b-8fe83429c9cd/json/12133/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/784ac114-5829-4f8e-85ba-d7bc6dc483b9/json/12138/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/68b0a2f8-b11b-4dab-a0a5-efdc27a1b66b/json/12141/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/6e6d9ff0-4fbd-4ac7-bbc2-4c3a95752f0a/json/12144/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/2f28c45c-ba28-4e61-858d-baba76bc47f5/json/12129/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/a8c32958-458b-4aa6-a549-77708be69a4b/json/12126/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/a20cd35f-0451-4a37-81ea-3f3d1312a43b/json/12128/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/6e827a58-3ec1-4451-a613-888982c2e4f6/json/12127/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/be228b58-fd58-4fe9-814b-1c8766c51627/json/12106/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/da63e36e-0a2b-4a4a-8b3a-d192e3c26b8c/json/12140/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/607a2b93-cc06-43fe-ba3d-33aeee731be9/json/12119/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/43171fcd-0423-42c9-a5ac-2615542b4802/json/12118/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'mpw': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/ef6fcdd2-edda-4ef7-83e9-194873a1a9cd/json/12174/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/d949e72d-23e1-49ac-bdfc-6a6fc1c7c299/json/12173/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/24fb07a9-66c8-4823-91bd-1c8c9f16a993/json/12194/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/0426fffc-531d-460a-80d6-dc6ac9b5eec3/json/12172/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/a9f25027-d8b7-4edd-b394-6840cd92eab8/json/12195/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/1ed7f5be-9b21-481e-9092-375fe62cae21/json/12183/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/f153f8e2-bd1c-4a34-a599-356b44f6668c/json/12184/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/68499612-c731-4430-a4d3-b1da4da4e6de/json/12181/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/d787c0ae-6fb8-448e-a4f6-8207e4b7db36/json/12182/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/0fb9251d-c0c6-4720-a5c9-64044c0f25be/json/12187/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/34f8e9b4-dfbd-4e66-a9c4-e34701ccc3e2/json/12190/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/8101a7b5-d5b8-4802-9385-954c75bbfb48/json/12193/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/846bf91d-6f12-47da-a617-27712c31360a/json/12178/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/04a1ace8-7252-4130-ab9d-4c044f0de6ac/json/12175/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/0311febd-ce1b-4af9-af0e-4c84f0eb2c3d/json/12177/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/9de5cc69-c12a-4530-9b08-bfc6a8da4d81/json/12176/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/5a9c40a4-289b-441b-ac8a-b52febf7aa74/json/12155/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/d734c7d9-abf4-457a-b0d3-d9f52013e15b/json/12189/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/0f1ad98e-bf43-4fc4-95c8-7b7e4f7fb582/json/12168/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/0a0f4e8a-71a8-41be-8423-7afd394fdfc5/json/12167/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'ktp': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/3964671b-334e-43be-95fe-8638643d4c46/json/11571/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/c8a43f5d-cf0d-4295-89d1-9b75b81b9b7c/json/11570/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/9dfdad4e-cf55-41d3-99c8-afd1281f2f28/json/11594/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/f49e81ff-5965-45f6-b7c7-6f3811111e32/json/11569/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/93eca963-ab83-4809-8b8d-0a6898dead60/json/11595/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/add4104b-4ed8-4252-8f29-bd4e2d0aa3d9/json/11581/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/074244e5-bdfd-471d-b9ca-22c85ba74787/json/11583/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/7ede83ab-a3ad-4ea0-b8fd-bcf4cef27596/json/11579/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/ecb4eefb-576c-44a2-9de6-2375f8adf04e/json/11580/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/7805898e-95e4-4b90-bdeb-042d46e34e74/json/11587/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/c1ace3c2-ed92-45ca-b65c-7580de1cc05c/json/11590/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/d100c8ba-545e-4582-9372-3eba55dff0ae/json/11593/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/06dd9374-5dba-469d-8e09-f5205777d286/json/11576/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/f01c022d-c463-4df7-810e-ddd65da2f82c/json/11573/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/f505d078-889c-49e4-8114-f1daa4431cc0/json/11575/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/3458c3d9-04bd-4616-aea6-16857931f57d/json/11574/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/79f5f568-ad6e-4ba8-9289-fa7bf50554c1/json/11551/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/2da8718d-4217-49cb-bc88-30a123b4aaa4/json/11589/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/4d456f5c-909d-4e8b-9a43-5e1be89e1266/json/11565/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/6b89666b-a30f-4014-b715-421450f598fb/json/11564/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
  },
  'ktn': {
    'urlSPSE_NonTenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/7a7c7a1f-58e2-4e4d-a305-85bf0698e895/json/9370/SPSE-NonTenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_NonTenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/04501a41-6dc0-4945-8022-df4a3948a54a/json/9369/SPSE-NonTenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesaiNilai' : "https://isb.lkpp.go.id/isb-2/api/b29277be-d53a-4940-a237-396a0e0cab20/json/9392/SPSE-TenderSelesaiNilai/tipe/4:4/parameter/",
    'urlSPSE_TenderPengumuman' : "https://isb.lkpp.go.id/isb-2/api/4e768df4-2cb8-4fce-a6e0-8813ccddebd8/json/9368/SPSE-TenderPengumuman/tipe/4:4/parameter/",
    'urlSPSE_TenderSelesai' : "https://isb.lkpp.go.id/isb-2/api/a2c7f0a1-99e6-4554-89a3-69696be87446/json/9393/SPSE-TenderSelesai/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTender' : "https://isb.lkpp.go.id/isb-2/api/dcfdf0d4-9f28-411f-b748-205db876bc06/json/9379/SPSE-PencatatanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PencatatanNonTenderRealisasi' : "https://isb.lkpp.go.id/isb-2/api/8b20940f-433d-4e31-bb4a-609c56118b98/json/9381/SPSE-PencatatanNonTenderRealisasi/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelola' : "https://isb.lkpp.go.id/isb-2/api/9ebd78a5-8190-4226-bf05-f7fd56db4b06/json/9377/SPSE-PencatatanSwakelola/tipe/4:4/parameter/",
    'urlSPSE_PencatatanSwakelolaRealisasi' : "https://isb.lkpp.go.id/isb-2/api/79b5bad1-df32-403b-9a39-2c3971d19f7e/json/9378/SPSE-PencatatanSwakelolaRealisasi/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanTender' : "https://isb.lkpp.go.id/isb-2/api/759c4f14-5b98-435a-a901-2a81b3d5a28e/json/9385/SPSE-JadwalTahapanTender/tipe/4:4/parameter/",
    'urlSPSE_JadwalTahapanNonTender' : "https://isb.lkpp.go.id/isb-2/api/26b5f199-9193-4a35-aa55-5089c4489e3c/json/9387/SPSE-JadwalTahapanNonTender/tipe/4:4/parameter/",
    'urlSPSE_PesertaTender' : "https://isb.lkpp.go.id/isb-2/api/6870c866-1a13-42f9-b35a-4e30cd7c46eb/json/9391/SPSE-PesertaTender/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/5c642c81-2f7f-4dad-bc20-7f789ce7bea9/json/9375/SPSE-TenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/d143d20b-1854-4001-86e5-b6120c324ed0/json/9372/SPSE-TenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/6dc88530-19a8-4e40-af59-877448cec955/json/9374/SPSE-TenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_TenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/29c018cc-e1ec-4a61-b343-aa9919bf2b40/json/9373/SPSE-TenderEkontrak-SPMKSPP/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakKontrak' : "https://isb.lkpp.go.id/isb-2/api/7d2166f4-c496-44c8-b36a-4806ed6278c5/json/9353/SPSE-NonTenderEkontrak-Kontrak/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPPBJ' : "https://isb.lkpp.go.id/isb-2/api/640bd9cf-2696-4c29-af8f-92d33dc741f0/json/9386/SPSE-NonTenderEkontrak-SPPBJ/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakBAPBAST' : "https://isb.lkpp.go.id/isb-2/api/b26192ab-cf92-437d-b006-09d1915dd711/json/9364/SPSE-NonTenderEkontrak-BAPBAST/tipe/4:4/parameter/",
    'urlSPSE_NonTenderEkontrakSPMKSPP' : "https://isb.lkpp.go.id/isb-2/api/6a97b843-2e9b-424d-9595-b4c9de032985/json/9363/SPSE-NonTenderEkontrak-SPMKSPP/tipe/4:4/parameter/"
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
    if jenisdata == "SPSENonTenderSelesai":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderSelesai']}{kodeJSON}"
    if jenisdata == "SPSENonTenderPengumuman":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderPengumuman']}{kodeJSON}"
    if jenisdata == "SPSETenderSelesaiNilai":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderSelesaiNilai']}{kodeJSON}"
    if jenisdata == "SPSETenderPengumuman":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderPengumuman']}{kodeJSON}"
    if jenisdata == "SPSETenderSelesai":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderSelesai']}{kodeJSON}"
    if jenisdata == "SPSEPencatatanNonTender":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_PencatatanNonTender']}{kodeJSON}"
    if jenisdata == "SPSEPencatatanNonTenderRealisasi":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_PencatatanNonTenderRealisasi']}{kodeJSON}"
    if jenisdata == "SPSEPencatatanSwakelola":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_PencatatanSwakelola']}{kodeJSON}"
    if jenisdata == "SPSEPencatatanSwakelolaRealisasi":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_PencatatanSwakelolaRealisasi']}{kodeJSON}"
    if jenisdata == "SPSEJadwalTahapanTender":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_JadwalTahapanTender']}{kodeJSON}"
    if jenisdata == "SPSEJadwalTahapanNonTender":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_JadwalTahapanNonTender']}{kodeJSON}"
    if jenisdata == "SPSEPesertaTender":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_PesertaTender']}{kodeJSON}"
    if jenisdata == "SPSETenderEkontrakKontrak":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderEkontrakKontrak']}{kodeJSON}"
    if jenisdata == "SPSETenderEkontrakSPPBJ":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderEkontrakSPPBJ']}{kodeJSON}"
    if jenisdata == "SPSETenderEkontrakBAPBAST":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderEkontrakBAPBAST']}{kodeJSON}"
    if jenisdata == "SPSETenderEkontrakSPMKSPP":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_TenderEkontrakSPMKSPP']}{kodeJSON}"
    if jenisdata == "SPSENonTenderEkontrakKontrak":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderEkontrakKontrak']}{kodeJSON}"
    if jenisdata == "SPSENonTenderEkontrakSPPBJ":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderEkontrakSPPBJ']}{kodeJSON}"
    if jenisdata == "SPSENonTenderEkontrakBAPBAST":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderEkontrakBAPBAST']}{kodeJSON}"
    if jenisdata == "SPSENonTenderEkontrakSPMKSPP":
      kodeJSON = f"{tahun}:{kodeLPSE}"
      urlFile = f"{url_data[kode]['urlSPSE_NonTenderEkontrakSPMKSPP']}{kodeJSON}"

      print(urlFile)

      return urlFile

kodes = ["PROV", "BKY", "MLW", "PTK", "SGU", "SKD", "KPH", "KKR", "LDK", "SKW", "STG", "MPW", "KTP", "KTN"]

kodes = [kode.lower() for kode in kodes]
jenisdatas = ["SPSENonTenderSelesai", "SPSENonTenderPengumuman", "SPSETenderSelesaiNilai", "SPSETenderPengumuman", "SPSETenderSelesai", "SPSEPencatatanNonTender", "SPSEPencatatanNonTenderRealisasi",
              "SPSEPencatatanSwakelola", "SPSEPencatatanSwakelolaRealisasi", "SPSEJadwalTahapanTender", "SPSEJadwalTahapanNonTender", "SPSEPesertaTender", "SPSETenderEkontrakKontrak",
              "SPSETenderEkontrakSPPBJ", "SPSETenderEkontrakBAPBAST", "SPSETenderEkontrakSPMKSPP", "SPSENonTenderEkontrakKontrak", "SPSENonTenderEkontrakSPPBJ", "SPSENonTenderEkontrakBAPBAST",
              "SPSENonTenderEkontrakSPMKSPP"]
tahuns = ["2022", "2023","2024"]

# Generate and save URLs to a text file
with open("generated_urls_spse.txt", "w") as file:
    for combination in product(jenisdatas, kodes, tahuns):
        url = generateURL(*combination)
        file.write(url + "\n")

print("URLs generated and saved to generated_urls.txt")








