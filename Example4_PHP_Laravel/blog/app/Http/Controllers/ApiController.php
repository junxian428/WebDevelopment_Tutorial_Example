<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ApiController extends Controller
{
    //
    public function getHello()
    {
        return ['message' => 'Hello, API!'];
    }
}
