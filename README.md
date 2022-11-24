## Backend FishApp
#### All team member were present during discussion via Discord

Anggota kelompok:

- Akmal Rafi Diara Putra
- Muhammad Izzat Azizan
- Delvino Ardi
- Muhammad Hadiid Faathir
- Rasyaad Maulana Khandiyas
- Narendra Arkan Putra Darmawan

## API Reference

#### Get all pond

```
  GET /pond
```

#### Get pond

```
  GET /pond/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Insert pond

```
  POST /pond
```

| Parameter  | Type     | Description  |
| :--------- | :------- | :----------- |
| `name`     | `string` | **Required** |
| `location` | `string` | **Required** |
| `shape`    | `string` | **Required** |
| `material` | `string` | **Required** |
